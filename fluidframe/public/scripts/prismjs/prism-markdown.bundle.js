!function(){"use strict";var e="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof window?window:"undefined"!=typeof global?global:"undefined"!=typeof self?self:{},n={exports:{}};!function(n){var t=function(e){var n=/(?:^|\s)lang(?:uage)?-([\w-]+)(?=\s|$)/i,t=0,a={},r={manual:e.Prism&&e.Prism.manual,disableWorkerMessageHandler:e.Prism&&e.Prism.disableWorkerMessageHandler,util:{encode:function e(n){return n instanceof o?new o(n.type,e(n.content),n.alias):Array.isArray(n)?n.map(e):n.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/\u00a0/g," ")},type:function(e){return Object.prototype.toString.call(e).slice(8,-1)},objId:function(e){return e.__id||Object.defineProperty(e,"__id",{value:++t}),e.__id},clone:function e(n,t){var a,o;switch(t=t||{},r.util.type(n)){case"Object":if(o=r.util.objId(n),t[o])return t[o];for(var i in a={},t[o]=a,n)n.hasOwnProperty(i)&&(a[i]=e(n[i],t));return a;case"Array":return o=r.util.objId(n),t[o]?t[o]:(a=[],t[o]=a,n.forEach((function(n,r){a[r]=e(n,t)})),a);default:return n}},getLanguage:function(e){for(;e;){var t=n.exec(e.className);if(t)return t[1].toLowerCase();e=e.parentElement}return"none"},setLanguage:function(e,t){e.className=e.className.replace(RegExp(n,"gi"),""),e.classList.add("language-"+t)},currentScript:function(){if("undefined"==typeof document)return null;if("currentScript"in document)return document.currentScript;try{throw new Error}catch(a){var e=(/at [^(\r\n]*\((.*):[^:]+:[^:]+\)$/i.exec(a.stack)||[])[1];if(e){var n=document.getElementsByTagName("script");for(var t in n)if(n[t].src==e)return n[t]}return null}},isActive:function(e,n,t){for(var a="no-"+n;e;){var r=e.classList;if(r.contains(n))return!0;if(r.contains(a))return!1;e=e.parentElement}return!!t}},languages:{plain:a,plaintext:a,text:a,txt:a,extend:function(e,n){var t=r.util.clone(r.languages[e]);for(var a in n)t[a]=n[a];return t},insertBefore:function(e,n,t,a){var o=(a=a||r.languages)[e],i={};for(var l in o)if(o.hasOwnProperty(l)){if(l==n)for(var s in t)t.hasOwnProperty(s)&&(i[s]=t[s]);t.hasOwnProperty(l)||(i[l]=o[l])}var u=a[e];return a[e]=i,r.languages.DFS(r.languages,(function(n,t){t===u&&n!=e&&(this[n]=i)})),i},DFS:function e(n,t,a,o){o=o||{};var i=r.util.objId;for(var l in n)if(n.hasOwnProperty(l)){t.call(n,l,n[l],a||l);var s=n[l],u=r.util.type(s);"Object"!==u||o[i(s)]?"Array"!==u||o[i(s)]||(o[i(s)]=!0,e(s,t,l,o)):(o[i(s)]=!0,e(s,t,null,o))}}},plugins:{},highlightAll:function(e,n){r.highlightAllUnder(document,e,n)},highlightAllUnder:function(e,n,t){var a={callback:t,container:e,selector:'code[class*="language-"], [class*="language-"] code, code[class*="lang-"], [class*="lang-"] code'};r.hooks.run("before-highlightall",a),a.elements=Array.prototype.slice.apply(a.container.querySelectorAll(a.selector)),r.hooks.run("before-all-elements-highlight",a);for(var o,i=0;o=a.elements[i++];)r.highlightElement(o,!0===n,a.callback)},highlightElement:function(n,t,a){var o=r.util.getLanguage(n),i=r.languages[o];r.util.setLanguage(n,o);var l=n.parentElement;l&&"pre"===l.nodeName.toLowerCase()&&r.util.setLanguage(l,o);var s={element:n,language:o,grammar:i,code:n.textContent};function u(e){s.highlightedCode=e,r.hooks.run("before-insert",s),s.element.innerHTML=s.highlightedCode,r.hooks.run("after-highlight",s),r.hooks.run("complete",s),a&&a.call(s.element)}if(r.hooks.run("before-sanity-check",s),(l=s.element.parentElement)&&"pre"===l.nodeName.toLowerCase()&&!l.hasAttribute("tabindex")&&l.setAttribute("tabindex","0"),!s.code)return r.hooks.run("complete",s),void(a&&a.call(s.element));if(r.hooks.run("before-highlight",s),s.grammar)if(t&&e.Worker){var c=new Worker(r.filename);c.onmessage=function(e){u(e.data)},c.postMessage(JSON.stringify({language:s.language,code:s.code,immediateClose:!0}))}else u(r.highlight(s.code,s.grammar,s.language));else u(r.util.encode(s.code))},highlight:function(e,n,t){var a={code:e,grammar:n,language:t};if(r.hooks.run("before-tokenize",a),!a.grammar)throw new Error('The language "'+a.language+'" has no grammar.');return a.tokens=r.tokenize(a.code,a.grammar),r.hooks.run("after-tokenize",a),o.stringify(r.util.encode(a.tokens),a.language)},tokenize:function(e,n){var t=n.rest;if(t){for(var a in t)n[a]=t[a];delete n.rest}var r=new s;return u(r,r.head,e),l(e,r,n,r.head,0),function(e){var n=[],t=e.head.next;for(;t!==e.tail;)n.push(t.value),t=t.next;return n}(r)},hooks:{all:{},add:function(e,n){var t=r.hooks.all;t[e]=t[e]||[],t[e].push(n)},run:function(e,n){var t=r.hooks.all[e];if(t&&t.length)for(var a,o=0;a=t[o++];)a(n)}},Token:o};function o(e,n,t,a){this.type=e,this.content=n,this.alias=t,this.length=0|(a||"").length}function i(e,n,t,a){e.lastIndex=n;var r=e.exec(t);if(r&&a&&r[1]){var o=r[1].length;r.index+=o,r[0]=r[0].slice(o)}return r}function l(e,n,t,a,s,g){for(var d in t)if(t.hasOwnProperty(d)&&t[d]){var p=t[d];p=Array.isArray(p)?p:[p];for(var f=0;f<p.length;++f){if(g&&g.cause==d+","+f)return;var h=p[f],m=h.inside,k=!!h.lookbehind,v=!!h.greedy,b=h.alias;if(v&&!h.pattern.global){var y=h.pattern.toString().match(/[imsuy]*$/)[0];h.pattern=RegExp(h.pattern.source,y+"g")}for(var w=h.pattern||h,x=a.next,_=s;x!==n.tail&&!(g&&_>=g.reach);_+=x.value.length,x=x.next){var E=x.value;if(n.length>e.length)return;if(!(E instanceof o)){var S,A=1;if(v){if(!(S=i(w,_,e,k))||S.index>=e.length)break;var C=S.index,$=S.index+S[0].length,L=_;for(L+=x.value.length;C>=L;)L+=(x=x.next).value.length;if(_=L-=x.value.length,x.value instanceof o)continue;for(var P=x;P!==n.tail&&(L<$||"string"==typeof P.value);P=P.next)A++,L+=P.value.length;A--,E=e.slice(_,L),S.index-=_}else if(!(S=i(w,0,E,k)))continue;C=S.index;var O=S[0],z=E.slice(0,C),M=E.slice(C+O.length),N=_+E.length;g&&N>g.reach&&(g.reach=N);var T=x.prev;if(z&&(T=u(n,T,z),_+=z.length),c(n,T,A),x=u(n,T,new o(d,m?r.tokenize(O,m):O,b,O)),M&&u(n,x,M),A>1){var R={cause:d+","+f,reach:N};l(e,n,t,x.prev,_,R),g&&R.reach>g.reach&&(g.reach=R.reach)}}}}}}function s(){var e={value:null,prev:null,next:null},n={value:null,prev:e,next:null};e.next=n,this.head=e,this.tail=n,this.length=0}function u(e,n,t){var a=n.next,r={value:t,prev:n,next:a};return n.next=r,a.prev=r,e.length++,r}function c(e,n,t){for(var a=n.next,r=0;r<t&&a!==e.tail;r++)a=a.next;n.next=a,a.prev=n,e.length-=r}if(e.Prism=r,o.stringify=function e(n,t){if("string"==typeof n)return n;if(Array.isArray(n)){var a="";return n.forEach((function(n){a+=e(n,t)})),a}var o={type:n.type,content:e(n.content,t),tag:"span",classes:["token",n.type],attributes:{},language:t},i=n.alias;i&&(Array.isArray(i)?Array.prototype.push.apply(o.classes,i):o.classes.push(i)),r.hooks.run("wrap",o);var l="";for(var s in o.attributes)l+=" "+s+'="'+(o.attributes[s]||"").replace(/"/g,"&quot;")+'"';return"<"+o.tag+' class="'+o.classes.join(" ")+'"'+l+">"+o.content+"</"+o.tag+">"},!e.document)return e.addEventListener?(r.disableWorkerMessageHandler||e.addEventListener("message",(function(n){var t=JSON.parse(n.data),a=t.language,o=t.code,i=t.immediateClose;e.postMessage(r.highlight(o,r.languages[a],a)),i&&e.close()}),!1),r):r;var g=r.util.currentScript();function d(){r.manual||r.highlightAll()}if(g&&(r.filename=g.src,g.hasAttribute("data-manual")&&(r.manual=!0)),!r.manual){var p=document.readyState;"loading"===p||"interactive"===p&&g&&g.defer?document.addEventListener("DOMContentLoaded",d):window.requestAnimationFrame?window.requestAnimationFrame(d):window.setTimeout(d,16)}return r}("undefined"!=typeof window?window:"undefined"!=typeof WorkerGlobalScope&&self instanceof WorkerGlobalScope?self:{});
/**
		 * Prism: Lightweight, robust, elegant syntax highlighting
		 *
		 * @license MIT <https://opensource.org/licenses/MIT>
		 * @author Lea Verou <https://lea.verou.me>
		 * @namespace
		 * @public
		 */n.exports&&(n.exports=t),void 0!==e&&(e.Prism=t)}(n),function(e){var n=/(?:\\.|[^\\\n\r]|(?:\n|\r\n?)(?![\r\n]))/.source;function t(e){return e=e.replace(/<inner>/g,(function(){return n})),RegExp(/((?:^|[^\\])(?:\\{2})*)/.source+"(?:"+e+")")}var a=/(?:\\.|``(?:[^`\r\n]|`(?!`))+``|`[^`\r\n]+`|[^\\|\r\n`])+/.source,r=/\|?__(?:\|__)+\|?(?:(?:\n|\r\n?)|(?![\s\S]))/.source.replace(/__/g,(function(){return a})),o=/\|?[ \t]*:?-{3,}:?[ \t]*(?:\|[ \t]*:?-{3,}:?[ \t]*)+\|?(?:\n|\r\n?)/.source;e.languages.markdown=e.languages.extend("markup",{}),e.languages.insertBefore("markdown","prolog",{"front-matter-block":{pattern:/(^(?:\s*[\r\n])?)---(?!.)[\s\S]*?[\r\n]---(?!.)/,lookbehind:!0,greedy:!0,inside:{punctuation:/^---|---$/,"front-matter":{pattern:/\S+(?:\s+\S+)*/,alias:["yaml","language-yaml"],inside:e.languages.yaml}}},blockquote:{pattern:/^>(?:[\t ]*>)*/m,alias:"punctuation"},table:{pattern:RegExp("^"+r+o+"(?:"+r+")*","m"),inside:{"table-data-rows":{pattern:RegExp("^("+r+o+")(?:"+r+")*$"),lookbehind:!0,inside:{"table-data":{pattern:RegExp(a),inside:e.languages.markdown},punctuation:/\|/}},"table-line":{pattern:RegExp("^("+r+")"+o+"$"),lookbehind:!0,inside:{punctuation:/\||:?-{3,}:?/}},"table-header-row":{pattern:RegExp("^"+r+"$"),inside:{"table-header":{pattern:RegExp(a),alias:"important",inside:e.languages.markdown},punctuation:/\|/}}}},code:[{pattern:/((?:^|\n)[ \t]*\n|(?:^|\r\n?)[ \t]*\r\n?)(?: {4}|\t).+(?:(?:\n|\r\n?)(?: {4}|\t).+)*/,lookbehind:!0,alias:"keyword"},{pattern:/^```[\s\S]*?^```$/m,greedy:!0,inside:{"code-block":{pattern:/^(```.*(?:\n|\r\n?))[\s\S]+?(?=(?:\n|\r\n?)^```$)/m,lookbehind:!0},"code-language":{pattern:/^(```).+/,lookbehind:!0},punctuation:/```/}}],title:[{pattern:/\S.*(?:\n|\r\n?)(?:==+|--+)(?=[ \t]*$)/m,alias:"important",inside:{punctuation:/==+$|--+$/}},{pattern:/(^\s*)#.+/m,lookbehind:!0,alias:"important",inside:{punctuation:/^#+|#+$/}}],hr:{pattern:/(^\s*)([*-])(?:[\t ]*\2){2,}(?=\s*$)/m,lookbehind:!0,alias:"punctuation"},list:{pattern:/(^\s*)(?:[*+-]|\d+\.)(?=[\t ].)/m,lookbehind:!0,alias:"punctuation"},"url-reference":{pattern:/!?\[[^\]]+\]:[\t ]+(?:\S+|<(?:\\.|[^>\\])+>)(?:[\t ]+(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|\((?:\\.|[^)\\])*\)))?/,inside:{variable:{pattern:/^(!?\[)[^\]]+/,lookbehind:!0},string:/(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|\((?:\\.|[^)\\])*\))$/,punctuation:/^[\[\]!:]|[<>]/},alias:"url"},bold:{pattern:t(/\b__(?:(?!_)<inner>|_(?:(?!_)<inner>)+_)+__\b|\*\*(?:(?!\*)<inner>|\*(?:(?!\*)<inner>)+\*)+\*\*/.source),lookbehind:!0,greedy:!0,inside:{content:{pattern:/(^..)[\s\S]+(?=..$)/,lookbehind:!0,inside:{}},punctuation:/\*\*|__/}},italic:{pattern:t(/\b_(?:(?!_)<inner>|__(?:(?!_)<inner>)+__)+_\b|\*(?:(?!\*)<inner>|\*\*(?:(?!\*)<inner>)+\*\*)+\*/.source),lookbehind:!0,greedy:!0,inside:{content:{pattern:/(^.)[\s\S]+(?=.$)/,lookbehind:!0,inside:{}},punctuation:/[*_]/}},strike:{pattern:t(/(~~?)(?:(?!~)<inner>)+\2/.source),lookbehind:!0,greedy:!0,inside:{content:{pattern:/(^~~?)[\s\S]+(?=\1$)/,lookbehind:!0,inside:{}},punctuation:/~~?/}},"code-snippet":{pattern:/(^|[^\\`])(?:``[^`\r\n]+(?:`[^`\r\n]+)*``(?!`)|`[^`\r\n]+`(?!`))/,lookbehind:!0,greedy:!0,alias:["code","keyword"]},url:{pattern:t(/!?\[(?:(?!\])<inner>)+\](?:\([^\s)]+(?:[\t ]+"(?:\\.|[^"\\])*")?\)|[ \t]?\[(?:(?!\])<inner>)+\])/.source),lookbehind:!0,greedy:!0,inside:{operator:/^!/,content:{pattern:/(^\[)[^\]]+(?=\])/,lookbehind:!0,inside:{}},variable:{pattern:/(^\][ \t]?\[)[^\]]+(?=\]$)/,lookbehind:!0},url:{pattern:/(^\]\()[^\s)]+/,lookbehind:!0},string:{pattern:/(^[ \t]+)"(?:\\.|[^"\\])*"(?=\)$)/,lookbehind:!0}}}}),["url","bold","italic","strike"].forEach((function(n){["url","bold","italic","strike","code-snippet"].forEach((function(t){n!==t&&(e.languages.markdown[n].inside.content.inside[t]=e.languages.markdown[t])}))})),e.hooks.add("after-tokenize",(function(e){"markdown"!==e.language&&"md"!==e.language||function e(n){if(n&&"string"!=typeof n)for(var t=0,a=n.length;t<a;t++){var r=n[t];if("code"===r.type){var o=r.content[1],i=r.content[3];if(o&&i&&"code-language"===o.type&&"code-block"===i.type&&"string"==typeof o.content){var l=o.content.replace(/\b#/g,"sharp").replace(/\b\+\+/g,"pp"),s="language-"+(l=(/[a-z][\w-]*/i.exec(l)||[""])[0].toLowerCase());i.alias?"string"==typeof i.alias?i.alias=[i.alias,s]:i.alias.push(s):i.alias=[s]}}else e(r.content)}}(e.tokens)})),e.hooks.add("wrap",(function(n){if("code-block"===n.type){for(var t="",a=0,r=n.classes.length;a<r;a++){var o=n.classes[a],u=/language-(.+)/.exec(o);if(u){t=u[1];break}}var c,g=e.languages[t];if(g)n.content=e.highlight((c=n.content,c.replace(i,"").replace(/&(\w{1,8}|#x?[\da-f]{1,8});/gi,(function(e,n){var t;if("#"===(n=n.toLowerCase())[0])return t="x"===n[1]?parseInt(n.slice(2),16):Number(n.slice(1)),s(t);var a=l[n];return a||e}))),g,t);else if(t&&"none"!==t&&e.plugins.autoloader){var d="md-"+(new Date).valueOf()+"-"+Math.floor(1e16*Math.random());n.attributes.id=d,e.plugins.autoloader.loadLanguages(t,(function(){var n=document.getElementById(d);n&&(n.innerHTML=e.highlight(n.textContent,e.languages[t],t))}))}}}));var i=RegExp(e.languages.markup.tag.pattern.source,"gi"),l={amp:"&",lt:"<",gt:">",quot:'"'},s=String.fromCodePoint||String.fromCharCode;e.languages.md=e.languages.markdown}(Prism);!function(e,n){void 0===n&&(n={});var t=n.insertAt;if(e&&"undefined"!=typeof document){var a=document.head||document.getElementsByTagName("head")[0],r=document.createElement("style");r.type="text/css","top"===t&&a.firstChild?a.insertBefore(r,a.firstChild):a.appendChild(r),r.styleSheet?r.styleSheet.cssText=e:r.appendChild(document.createTextNode(e))}}("code[class*=language-],pre[class*=language-]{word-wrap:normal;background:none;color:#f8f8f2;font-family:Consolas,Monaco,Andale Mono,Ubuntu Mono,monospace;font-size:1em;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;text-align:left;text-shadow:0 1px rgba(0,0,0,.3);white-space:pre;word-break:normal;word-spacing:normal}pre[class*=language-]{border-radius:.3em;margin:.5em 0;overflow:auto;padding:1em}:not(pre)>code[class*=language-],pre[class*=language-]{background:#272822}:not(pre)>code[class*=language-]{border-radius:.3em;padding:.1em;white-space:normal}.token.cdata,.token.comment,.token.doctype,.token.prolog{color:#8292a2}.token.punctuation{color:#f8f8f2}.token.namespace{opacity:.7}.token.constant,.token.deleted,.token.property,.token.symbol,.token.tag{color:#f92672}.token.boolean,.token.number{color:#ae81ff}.token.attr-name,.token.builtin,.token.char,.token.inserted,.token.selector,.token.string{color:#a6e22e}.language-css .token.string,.style .token.string,.token.entity,.token.operator,.token.url,.token.variable{color:#f8f8f2}.token.atrule,.token.attr-value,.token.class-name,.token.function{color:#e6db74}.token.keyword{color:#66d9ef}.token.important,.token.regex{color:#fd971f}.token.bold,.token.important{font-weight:700}.token.italic{font-style:italic}.token.entity{cursor:help}")}();
