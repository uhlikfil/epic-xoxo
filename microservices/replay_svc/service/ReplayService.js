'use strict';


/**
 * Add a new replay to the store
 *
 * body Replay Replay object to add
 * returns Replay
 **/
exports.add_replay = function(body) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "plays" : [ [ 0, 0 ], [ 0, 0 ] ]
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Deletes a replay
 *
 * replayId Long Replay id to delete
 * no response value expected for this operation
 **/
exports.delete_replay = function(replayId) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Search across all the replays
 * Filters through replays based on supplied filters. Returns abridged version of replays, where the specific turns (field `plays`) are not listed for brevity. If you need that, ask for a specific replay by its id. Also it is okay to use post method for liters because mongoDB does it too :)
 *
 * body ReplayFilter Filter criterions (optional)
 * returns ReplayArray
 **/
exports.filter_replays = function(body) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "date" : 1,
  "player1Id" : "player1Id",
  "player2Id" : "player2Id",
  "winnerId" : "winnerId",
  "id" : 0,
  "completed" : true,
  "startingId" : "startingId",
  "rounds" : 6
}, {
  "date" : 1,
  "player1Id" : "player1Id",
  "player2Id" : "player2Id",
  "winnerId" : "winnerId",
  "id" : 0,
  "completed" : true,
  "startingId" : "startingId",
  "rounds" : 6
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Get a replay by ID
 * Returns a single replay by its ID
 *
 * replayId Long ID of replay to return
 * returns Replay
 **/
exports.get_replay_by_id = function(replayId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "plays" : [ [ 0, 0 ], [ 0, 0 ] ]
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Update an existing replay
 *
 * body Replay Updates a replay based on the supplied ID. All fields in the schema are required.
 * no response value expected for this operation
 **/
exports.update_replay = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}

