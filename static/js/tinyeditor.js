tinymce.PluginManager.add('my-example-plugin', function (editor) {
    editor.ui.registry.addMenuItem('image', {
      icon: 'image',
      text: 'Image',
      onAction: function () {
        console.log('context menu clicked');
        alert('context menu clicked');
      }
    });
  
    editor.ui.registry.addContextMenu('image', {
      update: function (element) {
        return !element.src ? '' : 'image';
      }
    });
  });
  
tinymce.init({
    selector: '#myTextarea',
    height: 400,
    toolbar: 'h1 h2 bold italic strikethrough blockquote bullist numlist forecolor backcolor | link | removeformat ',
    menubar: false,
    paste_as_text: true,
    contextmenu: 'image',
    plugins: 'my-example-plugin',
});