const $medico = document.getElementById('user');
const $cmedico = document.getElementById('password');
$medico.onchange = showData;

function showData(){
 $cmedico.value = $medico.value;
}