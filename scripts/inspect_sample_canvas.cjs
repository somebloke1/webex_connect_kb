// Read an already loaded, explicitly temporary sample. Does not navigate or mutate.
const fs = require('node:fs/promises');
module.exports = async function captureSample(page, label, slug) {
  if (!/^[a-z0-9-]+$/.test(slug)) throw new Error('Invalid evidence slug');
  const record = await page.evaluate(() => {
    const editor = window.ui?.editor;
    if (!editor || !/^KBSample/.test(editor.filename)) throw new Error('Only explicitly temporary KBSample canvases may be captured');
    function safe(value, key = '') {
      if (/header|authorization|api[-_]?key|access.?token|auth.?token|password|secret|bot.access.token/i.test(key)) return '[redacted]';
      if (typeof value === 'string') {
        try { return safe(JSON.parse(value), key); } catch {}
        return value.replace(/https?:\/\/[^/\s"'<>]+/g, 'https://example.invalid')
          .replace(/([?&](?:auth_token|token|access_token)=)[^&\s"<>]+/gi, '$1[redacted]')
          .replace(/\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]+/g, '[redacted]')
          .replace(/default-dev-key/g, '[redacted]');
      }
      if (Array.isArray(value)) return value.map(v => safe(v));
      if (value && typeof value === 'object') {
        const namedSecret = typeof value.name === 'string' && /token|authorization|api.?key|password|secret/i.test(value.name);
        return Object.fromEntries(Object.entries(value).map(([k,v]) => [k,namedSecret && /value|default/i.test(k) ? '[redacted]' : safe(v,k)]));
      }
      return value;
    }
    function xml(element) {
      const name = element.getAttribute('name') || '';
      return {
        tag: element.tagName,
        attributes: safe(Object.fromEntries(Array.from(element.attributes).map(a => [a.name,a.value]))),
        text: element.children.length ? undefined : safe(element.textContent, element.tagName === 'header' ? 'header' : name),
        children: element.children.length ? Array.from(element.children).map(xml) : undefined
      };
    }
    return {
      flowId: editor.flowId,
      temporary_name: editor.filename,
      cells: Object.values(editor.graph.getModel().cells)
        .filter(c => c.edge || c.value?.nodeType === 1 || c.value?.nodeType === 'end' || c.value?.type === 'EN')
        .map(c => ({id:String(c.id),parent:c.parent?.id,vertex:!!c.vertex,edge:!!c.edge,source:c.source?.id,target:c.target?.id,value:c.value?.nodeType===1?xml(c.value):safe(c.value)})),
      customVariables: safe(editor.sessionData),
      outcomes: safe(editor.flowResultData)
    };
  });
  Object.assign(record, {label,observed_at:new Date().toISOString(),evidence_type:'read_only_inspection_of_loaded_sample_canvas_model',runtime_tested:false,redactions:'Header credentials, JWT-shaped strings (including parameter descriptions), and URL hosts redacted. Internal model properties are evidence, not a public import API.'});
  const dir = '/home/dgk/workspace/webex_connect_kb/evidence/sample-flows/observed';
  await fs.mkdir(dir,{recursive:true});
  await fs.writeFile(`${dir}/${slug}.json`, JSON.stringify(record,null,2)+'\n');
  return {label,flowId:record.flowId,cells:record.cells.length,nodes:record.cells.filter(c=>c.vertex).length,edges:record.cells.filter(c=>c.edge).length};
};
