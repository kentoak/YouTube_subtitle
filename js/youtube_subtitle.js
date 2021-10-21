
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