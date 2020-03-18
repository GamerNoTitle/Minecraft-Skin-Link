# Minecraft-Skin-Link

Since mojang changed the way to get user's skin, some plugins that require a new way to get the skin url, that's why i made this.

To use this program, please make sure that you've installed Python 3

Before you use it, open your cmd, powershell or any other thing and input the following command in it

```bash
$ pip install requests
```

this command will install ``requests`` package for python.

After you finish the installation, just type the command in the command line:

```bash
$ python main.py
```

and follow the tips to get the link.

If this project can do something helpful to you, would you mind to give me a Star?

---

Recently, we can use the ``http://skins.minecraft.net/MinecraftSkins/GamerNoTitle.png`` to get someone's skin, but now it will only return ``404 Not Found``.

According to the people on [Baidu Tieba](https://tieba.baidu.com/p/5843933209?red_tag=2201893003), if you want to get someone's skin, you should do these steps below:

- First: visit the website https://api.mojang.com/users/profiles/minecraft/GamerNoTitle to get someone's minecraft profile (GamerNoTitle is my username, you can change it to what username you want and really exists)

- Second: remember the uuid that the website returned to you. For example, when i visit the link above, it will return the message like this

  >```javascript
  >{"id":"35c432a4cf6b4485bef93957e7b7f509","name":"GamerNoTitle"}
  >```
  and the string behind ``id`` is my uuid.
  
- Third: visit the website https://sessionserver.mojang.com/session/minecraft/profile/35c432a4cf6b4485bef93957e7b7f509 to get the value which encrypted in base64 encoding. (35c432a4cf6b4485bef93957e7b7f509 is my uuid, you need to change it)

  It will return the message like this

  > ```javascript
  > {"id":"35c432a4cf6b4485bef93957e7b7f509","name":"GamerNoTitle","properties":[{"name":"textures","value":"eyJ0aW1lc3RhbXAiOjE1ODQ1MjUyNDM4ODUsInByb2ZpbGVJZCI6IjM1YzQzMmE0Y2Y2YjQ0ODViZWY5Mzk1N2U3YjdmNTA5IiwicHJvZmlsZU5hbWUiOiJHYW1lck5vVGl0bGUiLCJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjNmNWI4ZmExNDllMjA2NDZmMDRiNmQxMTFjMWQxODFhMTczY2U0YzRiMjkxZmZmZjFlMjI3MDY0NDMxMjc4YSIsIm1ldGFkYXRhIjp7Im1vZGVsIjoic2xpbSJ9fX19"}]}
  > ```

  and the string in ``value`` is what we need.
  
- Fourth: decode the value with base64, and you'll get the result like this

  > {"timestamp":1584526030943,"profileId":"35c432a4cf6b4485bef93957e7b7f509","profileName":"GamerNoTitle","textures":{"SKIN":{"url":"http://textures.minecraft.net/texture/b3f5b8fa149e20646f04b6d111c1d181a173ce4c4b291ffff1e227064431278a","metadata":{"model":"slim"}}}}

  they record the information about your skin, and the url in the result is the real link that connected to your skin.

  ![](http://textures.minecraft.net/texture/b3f5b8fa149e20646f04b6d111c1d181a173ce4c4b291ffff1e227064431278a)

