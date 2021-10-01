Dropzone.autoDiscover = false;

const myDropzone = new Dropzone("#my-dropzone", {
    url: "upload/",
    maxFiles: 3,
    maxFilesize: 50,
    acceptedFiles: '.png, .jpg',
    init: function () {
        // Set up any event handlers
        this.on("queuecomplete", function (file) {
      location.reload();
  });
    }
})