document.addEventListener("DOMContentLoaded", () => {
    const chatArea = document.getElementById("chat-area");
    const messageInput = document.getElementById("message-input");
    const chatForm = document.getElementById("chat-form");

    if (chatArea) {
        chatArea.scrollTop = chatArea.scrollHeight;
    }
    // making the option of Submit enabled even when "ENTER" key is pressed (without "Shift" key)
    if (messageInput && chatForm) {
        messageInput.addEventListener("keydown", (event) => {
            if (event.key === "Enter" && !event.shiftKey) {
                event.preventDefault();
                chatForm.requestSubmit();
            }
        });
    }
    // keep the message input box been focused anytime during the chat 
    chatForm.addEventListener("submit", () => {
        setTimeout(() => {
            messageInput.focus();
            if (chatArea) {
                chatArea.scrollTop = chatArea.scrollHeight;
            }
        }, 50);
    });

    // initial focus on the message input box
    messageInput.focus();

});
