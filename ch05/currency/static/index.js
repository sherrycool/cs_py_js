document.addEventListener('DOMContentLoaded', () => {
	document.querySelector('#form').onsubmit = () => {

		// Initialize new request
		const request = new XMLHttpRequest();
		const currency = document.querySelector('#currency').value;
		request.open('POST', '/convert'); 
		// 打开convert函数传出来的参数


		//callback function for when request complete
		request.onload = () =>{

			//extract json data from requrest, python传进来的参数
			const data = JSON.parse(request.responseText);  

			// update the result div
			if (data.success) {
				const contents = `1 CNY is equal to ${data.rate} ${currency}`;
				document.querySelector('#result').innerHTML = contents;
			}
			else {
				document.querySelector('#result').innerHTML = 'THere was an error.';
			}
		}
		// 上面只是定义如何操作 没有具体操作
		// add data to send with request
		// data changed
		const data = new FormData();
		data.append('currency', currency);

		//send request
		request.send(data)
		return false;
	}
})