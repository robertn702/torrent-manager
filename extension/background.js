chrome.contextMenus.create({
  id: 'add',
  contexts: ['link'],
  title: 'Add Torrent',
  onclick: addTorrent
});
