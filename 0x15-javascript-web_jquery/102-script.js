$('document').ready(function () {
	const url = 'https://www.fourtonfish.com/hellosalut/?';
	$('INPUT#btn_translate').click(function () {
		$.get(url + $.param({ lang: $('NPUT#language_code').val }), function (data) {
			$('DIV#hello').html(data.hello);
		});
	});
});
