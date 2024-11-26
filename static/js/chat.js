const formUser = document.getElementById("chat-form");
const inputUser = document.getElementById("user-input");
const messageContainer = document.getElementById("message-container");
const chatContainer = document.getElementById("chat-container");


const createMessageUi = (message) => {
  const div = document.createElement("div");
  div.className = "mt-10 space-y-3";
  div.innerHTML = `<div id="chat-container" class="flex items-center gap-x-2">
            <img
              class="rounded-full w-8 h-8 object-cover border border-gray-500"
              src="https://images.pexels.com/photos/91227/pexels-photo-91227.jpeg?auto=compress&cs=tinysrgb&w=50"
              alt=""
            />
            <p
              class="text-gray-100 bg-stone-800 p-3 rounded-lg shadow-md max-w-md"
            >
             ${message.message}
            </p>
          </div>
          <div class="flex flex-col">
            <i class="ri-sparkling-line text-yellow-400 text-2xl"></i>
            <p class="text-gray-100 hover:bg-stone-900 p-3  max-w-md typewriter">
              ${message.ai_message}
            </p>
          </div>
       `;
  messageContainer.appendChild(div);
};

inputUser.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    event.preventDefault(); 
    formUser.requestSubmit();
  }
});

formUser.addEventListener("submit", async (e) => {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);
  const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  const responseMessage = document.getElementById("response-message");

  try {
    const response = await fetch(form.action, {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfToken,
      },
      body: formData,
    });

    const data = await response.json();
    console.log(data);
    createMessageUi(data);
    chatContainer.scrollTo({
      top: chatContainer.scrollHeight,
      behavior: "smooth",
    });
    form.reset();
  } catch (error) {
    responseMessage.textContent = "Network error: " + error.message;
    responseMessage.style.color = "red";
  }
});

window.onload = () => {
  chatContainer.scrollTo({
    top: chatContainer.scrollHeight,
  });
};
