export function esc(value) { return String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
const list = value => Array.isArray(value) ? value.map(esc).join(', ') : esc(value);
export function Metric({title,value,delta}) { const sign=String(delta??'').trim().startsWith('-')?'down':'up'; return `<article class="card metric"><small>${esc(title)}</small><strong>${esc(value)}</strong><span class="${sign}">${esc(delta)}</span></article>`; }
export function Table({columns,rows}) { return `<article class="card"><table><thead><tr>${(columns??[]).map(c=>`<th>${esc(c)}</th>`).join('')}</tr></thead><tbody>${(rows??[]).map(r=>`<tr>${(r??[]).map(c=>`<td>${esc(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></article>`; }
export function Chart({kind,labels,values}) { return `<article class="card"><strong>${esc(kind)} chart</strong><p>${list(labels)}</p><p>${list(values)}</p></article>`; }
export const RENDERERS = {Metric,Table,Chart};
export function render(component, props) { return Object.hasOwn(RENDERERS, component) ? RENDERERS[component](props??{}) : `<article class="card error">unknown component: ${esc(component)}</article>`; }

