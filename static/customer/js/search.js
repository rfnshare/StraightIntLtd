const searchFun = () =>{
            let filter = document.getElementById('myInput').value;

            let dataTable = document.getElementById('dataTable');

            let tr = dataTable.getElementsByTagName('tr');

            for(var i=0; i<tr.length; i++)
            {
                let td = tr[i].getElementsByTagName('td')[1];

                if(td){
                    let textvlaue = td.textContent || td.innerHTML;

                    if(textvlaue.indexOf(filter) > -1){

                        tr[i].style.display = "";
                    }
                    else {
                        tr[i].style.display = "none";
                    }
                }
            }

        }