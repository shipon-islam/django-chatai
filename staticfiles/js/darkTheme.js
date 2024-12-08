const themeToggleDarkIcon = document.getElementById("theme-dark-icon");
const themeToggleLightIcon = document.getElementById("theme-light-icon");
const themeToggleBtn = document.getElementById("themetoggle");
if (themeToggleDarkIcon && themeToggleLightIcon && themeToggleBtn) {
  themeToggleBtn.addEventListener("click", function () {
    themeToggleDarkIcon.classList.toggle("hidden");
    themeToggleLightIcon.classList.toggle("hidden");
    const theme = localStorage.getItem("color-theme");
    if (theme) {
      if (theme === "light") {
        document.documentElement.classList.add("dark");
        localStorage.setItem("color-theme", "dark");
      } else {
        document.documentElement.classList.remove("dark");
        localStorage.setItem("color-theme", "light");
      }
    }
  });

  document.addEventListener("DOMContentLoaded", () => {
    themeToggleDarkIcon.classList.remove("hidden");
    themeToggleLightIcon.classList.add("hidden");
    document.documentElement.classList.add("dark");
    localStorage.setItem("color-theme", "dark");
  });
}