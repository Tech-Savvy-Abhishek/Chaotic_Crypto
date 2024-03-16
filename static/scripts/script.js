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
    var file = event.dataTransfer.files[0];
    previewFile(file);
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