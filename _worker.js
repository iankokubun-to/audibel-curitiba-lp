export default {async fetch(request,env){
 const url=new URL(request.url);
 if(url.hostname==="busca.audibelcuritiba.com.br" && (url.pathname==='/'||url.pathname==='/index.html')){
  const asset=new URL(request.url);asset.pathname='/black/';
  const response=await env.ASSETS.fetch(new Request(asset,request));
  const result=new Response(response.body,response);result.headers.set('Cache-Control','no-store');return result;
 }
 return env.ASSETS.fetch(request);
}};
