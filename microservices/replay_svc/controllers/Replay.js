'use strict';

var utils = require('../utils/writer.js');
var Replay = require('../service/ReplayService');

module.exports.add_replay = function add_replay(req, res, next, body) {
    Replay.add_replay(body)
        .then(function (response) {
            utils.writeJson(res, response);
        })
        .catch(function (response) {
            utils.writeJson(res, response);
        });
};

module.exports.delete_replay = function delete_replay(req, res, next, replayId, ok) {
    Replay.delete_replay(req.openapi.pathParams.replayId)
        .then(function (response) {
            utils.writeJson(res, response);
        })
        .catch(function (response) {
            utils.writeJson(res, response);
        });
};

module.exports.filter_replays = function filter_replays(req, res, next, body) {
    Replay.filter_replays(body)
        .then(function (response) {
            utils.writeJson(res, response);
        })
        .catch(function (response) {
            utils.writeJson(res, response);
        });
};

module.exports.get_replay_by_id = function get_replay_by_id(req, res, next, replayId) {
    Replay.get_replay_by_id(replayId)
        .then(function (response) {
            utils.writeJson(res, response);
        })
        .catch(function (response) {
            utils.writeJson(res, response);
        });
};

module.exports.update_replay = function update_replay(req, res, next, body) {
    Replay.update_replay(body)
        .then(function (response) {
            utils.writeJson(res, response);
        })
        .catch(function (response) {
            utils.writeJson(res, response);
        });
};
