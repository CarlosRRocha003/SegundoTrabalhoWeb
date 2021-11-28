const selectElement = document.querySelector('.datao');
console.log("AAAAAAAA");

selectElement.addEventListener('change', function () {
        console.log('awdqwj ');
        // recupera o campo username do formulário
        var campoDtNasc = document.getElementById('dtNasc');
        console.log('Mudou ', campoDtNasc.value);
        // cria o objeto HTTP Request e abre a conexão
        var xmlhttp = new XMLHttpRequest();
        console.log("{% url 'verificaDtNasc' %}?dtNasc=" + encodeURIComponent(campoDtNasc.value));
        xmlhttp.open("GET",'/verificaDtNasc?dtNasc=' + encodeURIComponent(campoDtNasc.value), true);
        // Função de callback
        xmlhttp.onreadystatechange = function () {
            if(xmlhttp.status == 200 && xmlhttp.readyState == 4) {
                var resposta = JSON.parse(xmlhttp.responseText);
                console.log("Resposta = " + resposta.valido);
            if (resposta.valido) {
                campoDtNasc.style = "border: 1px solid";
                document.getElementById('btnCria').disabled = false;
                document.getElementById('dtNascMsg').style.display = 'none';
            }
            else {
                campoDtNasc.style = "border: 1px solid #FF0000";
                document.getElementById('btnCria').disabled = true;
                document.getElementById('dtNascMsg').style.display = 'block';
            }
        }
        };
        // Envia o Request
        xmlhttp.send(null);
    });
