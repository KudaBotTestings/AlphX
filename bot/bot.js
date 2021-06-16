const Discord = require('discord.js');
const client = new Discord.Client();

var config = require('./config.js');
var configData = config.load();
    
function run() {
    client.on('ready', () => {
        console.log(`Logged in as ${client.user.tag}!`);
    });

    client.on('message', msg => {
        if (msg.content === 'ping') {
            msg.reply('Pong!');
        }
    });

    client.login(configData['token']);
}

exports.run = run;
exports.discord = Discord;
exports.client = client;