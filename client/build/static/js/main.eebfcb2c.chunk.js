(this.webpackJsonpclient=this.webpackJsonpclient||[]).push([[0],{15:function(e,t,c){},16:function(e,t,c){},19:function(e,t,c){"use strict";c.r(t);var n=c(1),r=c(2),s=c.n(r),i=c(4),d=c.n(i),a=(c(15),c.p,c(16),c(5)),j=c(6),l=c(9),o=c(8),h=c(21),b="http://localhost:5000/activeUsers";var u=function(e){Object(l.a)(c,e);var t=Object(o.a)(c);function c(e){var n;return Object(a.a)(this,c),(n=t.call(this,e)).state={error:null,isLoaded:!1,users:[]},n}return Object(j.a)(c,[{key:"componentDidMount",value:function(){var e=this;fetch(b).then((function(e){return e.json()})).then((function(t){console.log("success"),console.log(t),e.setState({users:t.users,isLoaded:!0})}),(function(t){e.setState({isLoaded:!0,error:t})}))}},{key:"getType",value:function(e){return e.is_admin?"admin":e.is_bot?"bot":"member"}},{key:"render",value:function(){var e=this,t=this.state.error,c=this.state.users,r=this.state.isLoaded;return console.log("data",c),t?Object(n.jsx)("div",{children:"Error Fetching"}):r?Object(n.jsx)("div",{children:Object(n.jsxs)(h.a,{id:"UserTable",dark:!0,responsive:!0,children:[Object(n.jsx)("thead",{children:Object(n.jsxs)("tr",{children:[Object(n.jsx)("th",{}),Object(n.jsx)("th",{children:"id"}),Object(n.jsx)("th",{children:"Full Name"}),Object(n.jsx)("th",{children:"Username"}),Object(n.jsx)("th",{children:"Role"}),Object(n.jsx)("th",{children:"Deleted"})]})}),Object(n.jsx)("tbody",{children:c.map((function(t){return Object(n.jsxs)("tr",{children:[Object(n.jsx)("td",{children:Object(n.jsx)("img",{src:t.profile.image_32})},t.id+"img"),Object(n.jsx)("td",{scope:"row",children:t.id},t.id),Object(n.jsx)("td",{children:t.real_name},t.id+"real_name"),Object(n.jsx)("td",{children:t.name},t.id+"name"),Object(n.jsx)("td",{children:e.getType(t)},t.id+"type"),Object(n.jsx)("td",{children:t.deleted?"true":"false"},t.id+"deleted")]},t.id+"user")}))})]})}):Object(n.jsx)("div",{children:"Loading..."})}}]),c}(s.a.Component);var O=function(){return Object(n.jsxs)("div",{className:"App",children:[Object(n.jsx)("header",{className:"App-header",children:"SlackTrack"}),Object(n.jsx)("div",{id:"centered-container",children:Object(n.jsx)(u,{})})]})};d.a.render(Object(n.jsx)(s.a.StrictMode,{children:Object(n.jsx)(O,{})}),document.getElementById("root"))}},[[19,1,2]]]);
//# sourceMappingURL=main.eebfcb2c.chunk.js.map