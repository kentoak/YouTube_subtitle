chrome.browserAction.onClicked.addListener(doActionButton);

function doActionButton(tab){
    console.log('Action Button clicked. Tab:',tab);
}

chrome.commands.onCommand.addListener(function(command) {
    //Polyfill the Browser Action button
    if(command === '_execute_browser_action') {
        chrome.tabs.query({active:true,currentWindow:true},function(tabs){
            //Get the popup for the current tab
            chrome.browserAction.getPopup({tabId:tabs[0].id},function(popupFile){
                if(popupFile){
                    openPopup(tabs[0],popupFile);
                } else {
                    //There is no popup defined, so we do what is supposed to be done for
                    //  the browserAction button.
                    doActionButton(tabs[0]);
                }
            });
        });
        return;
    } //else
});


chrome.contextMenus.onClicked.addListener(function(clickData){
    $(function(){
        var textArea = $('#changeText');
        textArea.on('keydown keyup keypress change focus blur click',function(){//keydown keyup keypress change: 入力エリアになにかしらの反応があった時のアクションを記述
            var self = $(this),
            text = self.val();//gオプションは置き換えたい文字列を指定した時にその文字が複数含まれている場合に、その全てを置き換えるオプション
            //let lit=text.split(/[\d\d:\d\d]/),
            var txt=text.replace(/\n/g,'').replace(/\d\d:\d\d/g,' ');
            console.log(txt);
            //console.log(lit),
            self.val(txt);
        });
    });
});
