/*1461678684,*/

if (self.CavalryLogger) { CavalryLogger.start_js(["cEK9F"]); }

__d('AccessibilityWebVirtualCursorClickLogger',['AccessibilityConfig','AccessibilityWebAssistiveTechTypedLogger','VirtualCursorStatus'],function a(b,c,d,e,f,g){if(c.__markCompiled)c.__markCompiled();var h={init:function(i){i.forEach(function(j){c('VirtualCursorStatus').add(j,this._log);}.bind(this),this);},_log:function(i,j){if(c('AccessibilityConfig').a11yVirtualCursorTrigger)if(i)new (c('AccessibilityWebAssistiveTechTypedLogger'))().setIndicatedBrowsers(j).log();}};f.exports=h;},null);