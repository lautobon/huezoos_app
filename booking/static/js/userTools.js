const userCardBtn = document.querySelector('.dropdown-user-card');
const petCardBtns = document.querySelectorAll('.three-dot-btn');

const initMenu = (element) => {

  const dropdown = M.Dropdown.init(element.target, {});

  dropdown.open();
}

userCardBtn.addEventListener('click', initMenu);


petCardBtns.forEach(btn => {
  btn.addEventListener('click', initMenu);
});
