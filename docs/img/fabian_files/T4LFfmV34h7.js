if (self.CavalryLogger) { CavalryLogger.start_js(["oQVVs"]); }

__d('AYMTFlyout',['Event'],(function a(b,c,d,e,f,g){var h={listen:function i(j,k){c('Event').listen(j,'click',k.show.bind(k));}};f.exports=h;}),null);
__d('AYMTRefreshElement',['csx','CSS','URI','DOM','DOMQuery','ge'],(function a(b,c,d,e,f,g,h){f.exports={init:function i(j,k){j.subscribe('itemclick',function(){c('CSS').addClass(k,'async_saving');});},initObjectSelector:function i(j,k){j.subscribe('itemclick',function(){var l=j.getFocusedItem(),m=new (c('URI'))(l._data.ajaxify).getQueryData(),n=m.promoted_object,o=c('DOMQuery').scry(c('ge')('aymt_object_section'),"._2eka img")[0],p=c('DOMQuery').scry(c('ge')('aymt_object_section'),"._2ekc a")[0],q=c('DOMQuery').scry(c('ge')('aymt_object_section'),"._q3r a")[0],r;if(p!==undefined){r=new (c('URI'))(p.dataset.hovercard);r.setQueryData({id:n});c('DOM').setAttributes(p,{'data-hovercard':r.toString()});c('DOM').setAttributes(p,{href:'#'});}else p=c('DOMQuery').scry(c('ge')('aymt_object_section'),"._2ekc span")[0];c('DOM').setContent(p,l._data.label);q&&c('DOM').setContent(q,null);if(o!==undefined){if(r===undefined){r=new (c('URI'))(o.parentNode.dataset.hovercard);r.setQueryData({id:n});}c('DOM').setAttributes(o,{src:l._data.iconsrc});c('DOM').setAttributes(o.parentNode,{'data-hovercard':r?r.toString():'#',href:'#'});}if(k===null)k=document.getElementById('aymt_object_info');c('CSS').addClass(k,'async_saving');});},initTimeRangeSelector:function i(j,k){j.subscribe('itemclick',function(){var l=j.getFocusedItem(),m=c('DOMQuery').scry(c('ge')('aymt_campaign_section'),"span ._2ekc")[0];c('DOM').setContent(m,l._data.label);c('CSS').addClass(k,'async_saving');});},fromLink:function i(j,k){j.onclick=function(){c('CSS').addClass(k,'async_saving');};}};}),null);
__d('AYMTHomepagePanelLogger',['BanzaiLogger','Event','tidyEvent'],(function a(b,c,d,e,f,g){var h=null,i={init:function j(k,l){c('tidyEvent')(c('Event').listen(k,'click',function(event){c('BanzaiLogger').log('AYMTHomepagePanelLoggerConfig',l);}));}};f.exports=i;}),null);
__d('HomepagePanelPageInsights.react',['cx','fbt','XUIButton.react','XUIButtonGroup.react','FacepileRounded.react','Link.react','List.react','PagesEventObserver','PagesEventType','React'],(function a(b,c,d,e,f,g,h,i){'use strict';var j,k,l=32,m={LIKE:'like',VIEW:'view',POST:'post'};j=babelHelpers.inherits(n,c('React').Component);k=j&&j.prototype;function n(o){k.constructor.call(this,o);this.state={selectedTab:m.LIKE};}n.prototype.render=function(){return c('React').createElement('div',null,this.$HomepagePanelPageInsights1(),this.$HomepagePanelPageInsights2());};n.prototype.$HomepagePanelPageInsights1=function(){return c('React').createElement('div',{className:"_2n5z"},c('React').createElement(c('XUIButtonGroup.react'),null,c('React').createElement(c('XUIButton.react'),{className:"_2n5-"+(this.state.selectedTab===m.LIKE?' '+"_2n60":''),label:i._("Likes"),onClick:this.$HomepagePanelPageInsights3.bind(this,m.LIKE)}),c('React').createElement(c('XUIButton.react'),{className:"_2n5-"+(this.state.selectedTab===m.VIEW?' '+"_2n60":''),label:i._("Views"),onClick:this.$HomepagePanelPageInsights3.bind(this,m.VIEW)}),c('React').createElement(c('XUIButton.react'),{className:"_2n5-"+(this.state.selectedTab===m.POST?' '+"_2n60":''),label:i._("Posts"),onClick:this.$HomepagePanelPageInsights3.bind(this,m.POST)})));};n.prototype.$HomepagePanelPageInsights2=function(){var o=c('React').createElement('div',{className:"_1oso"},this.props.date_range);switch(this.state.selectedTab){case m.LIKE:return c('React').createElement(c('List.react'),{border:'none',spacing:'none'},c('React').createElement('li',{className:"_2n66"},c('React').createElement(c('Link.react'),{className:"_2n67",href:this.props.insights_uri},this.props.total_likes)),c('React').createElement('li',{className:"_2n68"},c('React').createElement(c('Link.react'),{className:"_2n69"+(this.props.new_likes===0?' '+"_21t8":''),href:this.props.insights_uri},i._({"268435456":"1 new like this week","*":"{number} new likes this week"},[i.plural(this.props.new_likes,'number')]))),c('React').createElement('li',{className:"_2n6a"},c('React').createElement(c('Link.react'),{ajaxify:this.props.friend_inviter_uri,rel:'dialog'},c('React').createElement(c('FacepileRounded.react'),{imageSize:l,profiles:this.$HomepagePanelPageInsights4(),showNames:true}))));case m.VIEW:var p=c('React').createElement(c('Link.react'),{className:"_1osw"+(this.props.exceed_view_limit?' '+"_1osx":''),href:this.props.insights_uri},this.props.new_views),q=c('React').createElement(c('Link.react'),{className:"_1osz",href:this.props.insights_uri},i._({"268435456":" Page View","*":"Page Views"},[i.plural(this.props.new_views)])),r=c('React').createElement(c('Link.react'),{className:"_1osw"+(this.props.exceed_view_limit?' '+"_1osx":''),href:this.props.insights_uri},this.props.new_engagements),s=c('React').createElement(c('Link.react'),{className:"_1osz",href:this.props.insights_uri},i._({"268435456":" Post Engagement","*":"Post Engagements"},[i.plural(this.props.new_engagements)]));return c('React').createElement(c('List.react'),{border:'none',spacing:'none'},c('React').createElement('li',null,o),c('React').createElement('li',{className:"_1os-"},c('React').createElement(c('List.react'),{border:'light',direction:'horizontal',spacing:'none'},c('React').createElement('li',{className:"_1os_"},c('React').createElement(c('List.react'),{border:'none',spacing:'none'},c('React').createElement('li',null,p),c('React').createElement('li',null,q))),c('React').createElement('li',{className:"_1os_"},c('React').createElement(c('List.react'),{border:'none',spacing:'none'},c('React').createElement('li',null,r),c('React').createElement('li',null,s))))));case m.POST:var t=c('React').createElement(c('Link.react'),{className:"_1osw"+(this.props.exceed_post_limit?' '+"_1osx":''),href:this.props.insights_uri},this.props.new_comments),u=c('React').createElement(c('Link.react'),{className:"_1osz",href:this.props.insights_uri},i._({"268435456":" Comment","*":"Comments"},[i.plural(this.props.new_comments)])),v=c('React').createElement(c('Link.react'),{className:"_1osw"+(this.props.exceed_post_limit?' '+"_1osx":''),href:this.props.insights_uri},this.props.new_shares),w=c('React').createElement(c('Link.react'),{className:"_1osz",href:this.props.insights_uri},i._({"268435456":" Share","*":"Shares"},[i.plural(this.props.new_shares)]));return c('React').createElement(c('List.react'),{border:'none',spacing:'none'},c('React').createElement('li',null,o),c('React').createElement('li',{className:"_1os-"},c('React').createElement(c('List.react'),{border:'light',direction:'horizontal',spacing:'none'},c('React').createElement('li',{className:"_1os_"},c('React').createElement(c('List.react'),{border:'none',spacing:'none'},c('React').createElement('li',null,t),c('React').createElement('li',null,u))),c('React').createElement('li',{className:"_1os_"},c('React').createElement(c('List.react'),{border:'none',spacing:'none'},c('React').createElement('li',null,v),c('React').createElement('li',null,w))))));default:return c('React').createElement('div',null);}};n.prototype.$HomepagePanelPageInsights4=function(){var o=this.props.friends_data;return Object.keys(o).map(function(p){return {image_src:'https://graph.facebook.com/'+o[p].uniqueID+'/picture?height='+l*2+'&width='+l*2,name:o[p].name};});};n.prototype.$HomepagePanelPageInsights3=function(o){this.setState({selectedTab:o});c('PagesEventObserver').notify(c('PagesEventType').VISIT_INSIGHTS_TAB,this.props.page_id,{ref:'aymt_homepage_panel'});};f.exports=n;}),null);
__d('PagesRecentPostsActionBar',['React','ReactDOM','TrackingNodes','UFIReactionsBlingSocialSentence.react','URI','goURI'],(function a(b,c,d,e,f,g){'use strict';h.prototype.render=function(i,j,k,l,m){var n=c('TrackingNodes').getTrackingInfo(c('TrackingNodes').types.BLINGBOX);if(j.showtheaterforcomment&&j.commentredirecturi){j.commentajaxify=j.commentredirecturi;j=Object.freeze(j);}var o=l,p=(j.feedbackMode==='none'||j.feedbackMode==='toggle')&&j.hasReactions&&k.displayreactions,q=function r(event){c('goURI')(new (c('URI'))(m));};if(p)c('ReactDOM').render(c('React').createElement(c('UFIReactionsBlingSocialSentence.react'),{commentCount:o,contextArgs:j,'data-comment-prelude-ref':'action_link_bling','data-ft':n,feedback:k,href:m,onCommentClick:q}),i);};function h(){}f.exports=new h();}),null);