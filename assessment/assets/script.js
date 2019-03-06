$('document').ready(function(){
    var random=0;
    var colors=['#16a085', '#27ae60', '#2c3e50', '#f39c12', '#e74c3c', '#9b59b6', '#FB6964', '#342224', "#472E32", "#BDBB99", "#77B1A9", "#73A857"];
    $('button').on("click",function(){
      
      if(random !=11)
      random++
      else
        random=0;
  
      $('body').css("background-color",colors[random]);
        $('button').css("background-color",colors[random]);
        $('a').css("background-color",colors[random]);
        $('#myquote').css("color",colors[random]);
     $('.fa-quote-left').css("color",colors[random]);  
     $.ajax({
      url: "https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous",
        headers: {"X-Mashape-Key": "nsXHHzarDAmshL6wXG7PnD7OH512p1qlXXIjsn1nX8Ljdlb1b9"}
    }).done(function(json){
    $('#myquote').html(json.quote);
    $('.blockquote-footer').html(json.author)   
   
    });
    });
  });