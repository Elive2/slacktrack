(this.webpackJsonpclient=this.webpackJsonpclient||[]).push([[0],{19:function(e,t,c){},20:function(e,t,c){},23:function(e,t,c){"use strict";c.r(t);var s=c(1),i=c(2),n=c.n(i),r=c(9),d=c.n(r),a=(c(19),c.p,c.p+"static/media/GitHub_Logo_White.6149aa5c.png"),j=(c(20),c(10)),o=c(11),l=c(13),h=c(12),b=c(25),u=c(26),O=function(e){Object(l.a)(c,e);var t=Object(h.a)(c);function c(e){var s;return Object(j.a)(this,c),(s=t.call(this,e)).fetchUsers=function(){fetch("http://167.71.127.136:5000/activeUsers").then((function(e){return e.json()})).then((function(e){console.log("success"),console.log(e),s.setState({users:e.users,isLoaded:!0})}),(function(e){s.setState({isLoaded:!0,error:e})}))},s.state={error:null,isLoaded:!1,users:[]},s}return Object(o.a)(c,[{key:"componentDidMount",value:function(){this.fetchUsers()}},{key:"getType",value:function(e){return e.is_admin?"admin":e.is_bot?"bot":"member"}},{key:"render",value:function(){var e=this,t=this.state.error,c=this.state.users,i=this.state.isLoaded;return console.log("data",c),t?Object(s.jsx)("div",{children:"Error Fetching"}):i?Object(s.jsxs)("div",{children:[Object(s.jsxs)(b.a,{id:"UserTable",dark:!0,responsive:!0,children:[Object(s.jsx)("thead",{children:Object(s.jsxs)("tr",{children:[Object(s.jsx)("th",{}),Object(s.jsx)("th",{children:"id"}),Object(s.jsx)("th",{children:"Full Name"}),Object(s.jsx)("th",{children:"Username"}),Object(s.jsx)("th",{children:"Role"}),Object(s.jsx)("th",{children:"Deleted"})]})}),Object(s.jsx)("tbody",{children:c.map((function(t){return Object(s.jsxs)("tr",{children:[Object(s.jsx)("td",{children:Object(s.jsx)("img",{src:t.profile.image_32})},t.id+"img"),Object(s.jsx)("td",{scope:"row",children:t.id},t.id),Object(s.jsx)("td",{children:t.real_name},t.id+"real_name"),Object(s.jsx)("td",{children:t.name},t.id+"name"),Object(s.jsx)("td",{children:e.getType(t)},t.id+"type"),Object(s.jsx)("td",{children:t.deleted?"true":"false"},t.id+"deleted")]},t.id+"user")}))})]}),Object(s.jsx)(u.a,{onClick:this.fetchUsers,children:"Refresh"})]}):Object(s.jsx)("div",{children:"Loading..."})}}]),c}(n.a.Component);var x=function(){return Object(s.jsxs)("div",{className:"App",children:[Object(s.jsxs)("header",{className:"App-header",children:["SlackTrack",Object(s.jsx)("div",{id:"GitLogo",children:Object(s.jsx)("a",{href:"https://github.com/Elive2/slacktrack/",target:"_blank",children:Object(s.jsx)("img",{id:"GitLogoImg",src:a})})})]}),Object(s.jsx)("div",{id:"centered-container",children:Object(s.jsx)(O,{})})]})};d.a.render(Object(s.jsx)(n.a.StrictMode,{children:Object(s.jsx)(x,{})}),document.getElementById("root"))}},[[23,1,2]]]);
//# sourceMappingURL=main.a87c228e.chunk.js.map