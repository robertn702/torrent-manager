'use strict';

var ADD_URL = 'http://73.170.182.244/torrent/download?url=';

chrome.contextMenus.create({
  id: 'add',
  contexts: ['link'],
  title: 'Add Torrent'
});

chrome.contextMenus.onClicked.addListener(function(e) {
  // console.log('[background] url: ', ADD_URL + encodeURI(e.linkUrl));
  $.get(ADD_URL + e.linkUrl)
    .done(function() {
      console.log('[background] Torrent Added');
    });
});
