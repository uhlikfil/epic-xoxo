'use strict';

const db = require('../database/pg')

/**
 * Add a new replay to the store
 *
 * body Replay Replay object to add
 * returns Replay
 **/
exports.add_replay = function (body) {
    return new Promise(function (resolve, reject) {
        let err = checkKeysPresent(KEYS_NO_ID, body)
        if (err.length == 0) {
            body.date = new Date(body.date)
            body.plays = JSON.stringify(body.plays)
            db.insertReplay(body)
                .then(value => resolve())
                .catch(reason => reject(reason))
        }
        else {
            reject(400)
        }
    });
}


/**
 * Deletes a replay
 *
 * replayId Long Replay id to delete
 * no response value expected for this operation
 **/
exports.delete_replay = function (replayId) {
    return new Promise(function (resolve, reject) {
        db.deleteReplay(replayId)
            .then(
                value => resolve()
            )
            .catch(reason => reject(reason))
    });
}


/**
 * Search across all the replays
 * Filters through replays based on supplied filters. Returns abridged version of replays, where the specific turns
 * (field `plays`) are not listed for brevity. If you need that, ask for a specific replay by its id. Also it is okay
 * to use post method for liters because mongoDB does it too :)
 *
 * body ReplayFilter Filter criterions (optional)
 * returns ReplayArray
 **/
exports.filter_replays = function (body) {
    return new Promise(function (resolve, reject) {
            let sql = 'select * from replays';
            let wheres = []
            if (body === undefined) {
                reject(400);
                return
            }
            if (body.player1Id) {
                console.log('wtf');
                wheres.push(['player1Id=', body.player1Id]);
            }
            if (body.player2Id) {wheres.push(['player2Id=', body.player2Id])}
            if (body.winnerId) {wheres.push(['winnerId=', body.winnerId])}
            if (body.startingId) {wheres.push(['startingId=', body.startingId])}
            if (body.completed) {wheres.push(['completed=', body.completed])}
            if (body.date) {
                if (body.date.before) {
                    body.date.before = new Date(body.date.before)
                    wheres.push(['date <', body.date.before])
                }
                if (body.date.after) {
                    body.date.after = new Date(body.date.after)
                    wheres.push(['date >', body.date.after])
                }
            }
            if (body.rounds) {
                if (body.rounds.gte) {
                    wheres.push(['rounds >=', body.rounds.gte])
                }
                if (body.rounds.lte) {
                    wheres.push(['rounds <=', body.rounds.lte])
                }
            }
            const values = []
            for (let x of wheres) {
                values.push(x[1])
            }
            wheres = wheres.map((value, index) => value[0] + '$' + (index + 1))
            if (wheres.length > 0) {
                sql += ' where '
            }
            sql += wheres.join(' AND ')
            sql += ' ORDER BY date DESC';
            db.customQuery(sql, values)
                .then((value) => {
                    resolve(value.rows)
                })
                .catch((reason) => {
                        reject(400)
                    }
                )
        }
    );
}


/**
 * Get a replay by ID
 * Returns a single replay by its ID
 *
 * replayId Long ID of replay to return
 * returns Replay
 **/
exports.get_replay_by_id = function (replayId) {
    return new Promise(function (resolve, reject) {
        db.findReplayById(replayId)
            .then((v) => {
                if (v.rows.length > 0) {
                    resolve(v.rows[0])
                }
                else {
                    reject(404)
                }
            })
            .catch((reason) => {
                reject(reason)
            })
    });
}


/**
 * Update an existing replay
 *
 * body Replay Updates a replay based on the supplied ID. All fields in the schema are required.
 * no response value expected for this operation
 **/
exports.update_replay = function (body) {
    return new Promise(function (resolve, reject) {
        let missing = checkKeysPresent(KEYS, body)
        if (missing.length == 0) {
            body.date = new Date(body.date)
            body.plays = JSON.stringify(body.plays)
            db.putReplay(body.id, body)
                .then((v) => {resolve(200)})
                .catch((e) => {
                    console.log(e);
                    reject(404)
                })
        }
        else {
            reject(400)
        }
    });
}

const KEYS = ['id', 'player1Id', 'player2Id', 'winnerId', 'startingId', 'rounds', 'plays', 'completed', 'date']
const KEYS_NO_ID = ['player1Id', 'player2Id', 'winnerId', 'startingId', 'rounds', 'plays', 'completed', 'date']

function checkKeysPresent(keys, obj) {
    let errs = []
    for (let k of keys) {
        if (obj[k] === undefined) errs.push('k')
    }
    return errs;
}
