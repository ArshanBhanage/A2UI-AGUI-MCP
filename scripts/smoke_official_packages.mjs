const checks = [
  ['@openuidev/react-lang', ['defineComponent', 'createLibrary', 'parseMessage']],
  ['@json-render/core', ['applySpecPatch', 'validateSpec']],
  ['@modelcontextprotocol/ext-apps', ['App', 'McpUiHostContextSchema']],
];
for (const [name, keys] of checks) {
  const mod = await import(name);
  const missing = keys.filter(key => !mod[key]);
  if (missing.length) throw new Error(`${name}: missing ${missing.join(', ')}`);
  console.log(`${name}: ${keys.join(', ')} verified`);
}
