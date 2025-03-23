const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});
localStorage.clear(); // لمسح جميع البيانات المخزنة في LocalStorage
sessionStorage.clear(); // لمسح البيانات المخزنة في SessionStorage
