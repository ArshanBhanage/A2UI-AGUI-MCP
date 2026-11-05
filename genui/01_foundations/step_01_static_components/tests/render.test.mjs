import test from 'node:test'; import assert from 'node:assert/strict'; import {Metric,render} from '../page/render.mjs';
test('escapes model props',()=>assert.match(Metric({title:'<x>',value:'1',delta:'+1'}),/&lt;x&gt;/));
test('unknown component is visible and safe',()=>assert.match(render('constructor',{x:'<script>'}),/unknown component/));

