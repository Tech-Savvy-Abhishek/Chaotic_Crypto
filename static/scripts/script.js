window.onbeforeunload = function ()
{
    window.scrollTo(0, 0);
};

document.getElementById('menuButton').addEventListener('click', function ()
{
    document.getElementById('menu').classList.toggle('hidden');
});

document.getElementById('closeButton').addEventListener('click', function ()
{
    document.getElementById('menu').classList.add('hidden');
});

document.getElementById('numbers').addEventListener('input', function (e)
{
    var numbers = e.target.value.split(',');
    var coloredNumbers = numbers.map(function (number, index)
    {
        return '<span class="number-' + (index + 1) + '">' + number.trim() + '</span>';
    });
    document.getElementById('coloredNumbers').innerHTML = coloredNumbers.join(', ');
});



document.getElementById('drop_zone').addEventListener('dragover', function (event)
{
    event.stopPropagation();
    event.preventDefault();
    event.dataTransfer.dropEffect = 'copy';
});


document.getElementById('drop_zone').addEventListener('drop', function (event)
{
    event.stopPropagation();
    event.preventDefault();
    var originalFile = event.dataTransfer.files[0];

    // Read the original file as a Blob object
    var blob = new Blob([originalFile], { type: originalFile.type });

    // Create a new File object with the correct MIME type
    var file = new File([blob], originalFile.name, { type: originalFile.type });

    previewFile(file);

    // Create a new (empty) FileList object
    var fileList = new DataTransfer();

    // Add the file to the FileList object
    fileList.items.add(file);

    // Assign the FileList to the 'file' input field
    document.getElementById('fileInput').files = fileList.files;
});


function previewFile(file)
{
    var reader = new FileReader();
    reader.onloadend = function ()
    {
        document.getElementById('preview').src = reader.result;
        document.getElementById('preview').style.display = 'block';
        document.getElementById('drag-and-drop-illustration').style.display = 'none';
        document.getElementById('drag-and-drop-guide').style.display = 'none';
    };
    reader.readAsDataURL(file);
}

document.getElementById('fileInput').addEventListener('change', function (event)
{

    var file = event.target.files[0];
    previewFile(file);
});