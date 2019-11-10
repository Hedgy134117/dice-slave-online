const tokenProvider = new Chatkit.TokenProvider({
    url:
    "https://us1.pusherplatform.io/services/chatkit_token_provider/v1/a8bf6e00-9030-4db8-9582-a41e9741b892/token"
});

const chatManager = new Chatkit.ChatManager({
    instanceLocator: "v1:us1:a8bf6e00-9030-4db8-9582-a41e9741b892",
    userId: "admin",
    tokenProvider: tokenProvider
});

chatManager.connect()
.then(currentUser => {
    currentUser.subscribeToRoomMultipart({
        roomId: currentUser.rooms[0].id,
        hooks: {
            onMessage: message => {
                const ul = document.getElementById("messages");
                const li = document.createElement("li");
                var messageContent = message.parts[0].payload.content;
                var name = ""
                var text = ""

                var foundName = false;
                for (var i = 0; i < messageContent.length; i++) {
                    console.log(messageContent.charAt(i));
                    if (messageContent.charAt(i) == "/") {
                        foundName = true;
                        continue;
                    }
                    if (foundName === false) {
                        name += messageContent.charAt(i);
                    }
                    else {
                        text += messageContent.charAt(i);
                    }
                }

                li.appendChild(
                    document.createTextNode(name + ': ' + text)
                );
                ul.appendChild(li);
            }
        }
    });

    const d4 = document.getElementById("d4");
    d4.addEventListener("click", e => {
        e.preventDefault();
        const name = document.getElementById('name');

        currentUser.sendSimpleMessage ({
            text: name.value + "/" + "1d4 - " + (Math.floor(Math.random() * 4) + 1),
            roomId: currentUser.rooms[0].id
        })
    })

    const d6 = document.getElementById("d6");
    d6.addEventListener("click", e => {
        e.preventDefault();
        const name = document.getElementById('name');

        currentUser.sendSimpleMessage ({
            text: name.value + "/" + "1d6 - " + (Math.floor(Math.random() * 6) + 1),
            roomId: currentUser.rooms[0].id
        })
    })

    const d10 = document.getElementById("d10");
    d10.addEventListener("click", e => {
        e.preventDefault();
        const name = document.getElementById('name');

        currentUser.sendSimpleMessage ({
            text: name.value + "/" + "1d10 - " + (Math.floor(Math.random() * 10) + 1),
            roomId: currentUser.rooms[0].id
        })
    })

    const d12 = document.getElementById("d12");
    d12.addEventListener("click", e => {
        e.preventDefault();
        const name = document.getElementById('name');

        currentUser.sendSimpleMessage ({
            text: name.value + "/" + "1d12 - " + (Math.floor(Math.random() * 12) + 1),
            roomId: currentUser.rooms[0].id
        })
    })

    const d20 = document.getElementById("d20");
    d20.addEventListener("click", e => {
        e.preventDefault();
        const name = document.getElementById('name');

        currentUser.sendSimpleMessage ({
            text: name.value + "/" + "1d20 - " + (Math.floor(Math.random() * 20) + 1),
            roomId: currentUser.rooms[0].id
        })
    })

    const d100 = document.getElementById("d100");
    d100.addEventListener("click", e => {
        e.preventDefault();
        const name = document.getElementById('name');

        currentUser.sendSimpleMessage ({
            text: name.value + "/" + "1d100 - " + (Math.floor(Math.random() * 100) + 1),
            roomId: currentUser.rooms[0].id
        })
    })
})
.catch(error => {
    console.error("error:", error);
})