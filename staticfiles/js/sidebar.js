    const menubtn = document.querySelector("#conversation-menu");
    const sidebar = document.querySelector(".sidebar");
  menubtn.addEventListener("click", () => {
    sidebar.classList.toggle("active");
  });
    function debounce(func, delay) {
    let timeoutId;

    return function (...args) {
      const context = this;
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        func.apply(context, args);
      }, delay);
    };
  }
  function widthCheck() {
    if (window.innerWidth < 650) {
      sidebar.classList.toggle("active");
    } else {
      sidebar.classList.remove("active");
    }
  }
  window.addEventListener("DOMContentLoaded",()=>{
    widthCheck()
  })
  window.addEventListener("resize", debounce(widthCheck, 300));