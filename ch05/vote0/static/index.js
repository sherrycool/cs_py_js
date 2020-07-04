document.addEventListener('DOMContentLoaded', ()=>{

	//connect to webbsocket
	var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

	// when connected, confiture buttons
	socket.on('connect', () =>{

		//each button should emit a "submit vote"
		document.querySelectorAll('button').forEach(button =>{
			button.onclick = () =>{
				const selection = button.dataset.vote;
				// 传给webserver
				socket.emit('submit vote', {'selection':selection});
			};
		});
	});

	// when a new vote is announed, add to the unorderd List
	socket.on('announce vote', data => {
		const li = document.createElement('li');
		li.innerHTML = `Vote recorded: ${data.selection}`;
		document.querySelector('#votes').append(li);
	});
});

