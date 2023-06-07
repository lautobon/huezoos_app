const headerBtn = document.querySelector('.top .three-dot-btn');

headerBtn.addEventListener('click', (event) => {

  const dropdown = M.Dropdown.init(element.target, {});

  dropdown.open();
});