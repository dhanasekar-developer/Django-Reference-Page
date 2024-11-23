console.log('Api data')
function loadData(empcode){
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.log(empcode)
    $.ajax({
        url: "/api/data/",
        method: "POST",
        data: {
            empcode: empcode,
            csrfmiddlewaretoken: csrf_token 
        },success:function(respose){
            console.log(respose)

            const tableView = document.getElementById('tableView');
            tableView.innerHTML='';
            const div = document.createElement('div')
            div.innerHTML = respose;
            tableView.appendChild(div)
            // console.log('success : ',respose)
            // const tbody = document.getElementById('tbody');
            // respose.datas.forEach(data => {
            //     const row = document.createElement('tr');

            //     row.innerHTML = `
            //     <td>${data.EMPCODE}</td>
            //     <td>${data.EMPNAME}</td>
            //     <td>${data.PHONE}</td>
            //     <td>${data.EMAIL}</td>
            //     `
            //     tbody.appendChild(row)
            // });
            // tableView.style.display = 'table';
        }
    });
}

function colorFieldFunction(){
    colorField = document.getElementById('colorField').value;
    console.log(colorField)
}