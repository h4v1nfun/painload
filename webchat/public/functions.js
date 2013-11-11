function inputParser (str) {
  var match = /^\/([a-z]+)(?:\s+(.*\S))?\s*$/.exec(str)
  if (match) {
    return { method: match[1], params: match[2] }
  } else {
    return { method: 'say', params: str }
  }
}


function clientParser(object) {
    console.log('parser: ',object)
    return (handler[object.method] || console.log)(object.params)
//switch (object.method) {
//  case 'message':
//    return handler.message(object.params);
//  case 'join':
//    return handler.join(object.params);
//  case 'quit':
//    return handler.quit(object.params);
//  case 'nicklist': 
//    return handler.nicklist(object.params);
//  case 'nickchange':
//    return handler.nickchange(object.params);
//}
};


function replaceURLWithHTMLLinks (text) {
  var exp = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig;
  return text.replace(exp,"<a class=chat_link href='$1'>$1</a>");
}

function setMaybeNick (input) {
  if (match) {
    nick = match[1];
    $('#nick').html(nick);
  }
}
function sortNicklist () {
};

function getNicklistElement(name) { 
  var el;
  $('.name').each(function (i,e) {
    if (e.innerHTML === name) {
      if (typeof el !== 'undefined') {
        throw new Error('duplicate name: ' + name);
      };
      el = e;
    };
  });
  return el;
}

function chatboxAppend (chat_from, chat_msg, type) {
  type = type||'chat'
  $('<tr><td class="'+type+'_date">'+getCurTime()+'</td><td class="'+type+'_from">'+chat_from+'</td><td class="'+type+'_msg">'+chat_msg+'</td></tr>').insertBefore('#foot');

  var elem = document.getElementById('chatter');
  elem.scrollTop = elem.scrollHeight;
};

function getCurTime () {
  date = new Date;
  h = date.getHours();
  if(h<10)
  {
    h = "0"+h;
  }
  m = date.getMinutes();
  if(m<10)
  {
    m = "0"+m;
  }
  s = date.getSeconds();
  if(s<10)
  {
    s = "0"+s;
  }
  return ''+h+':'+m+':'+s;
};
