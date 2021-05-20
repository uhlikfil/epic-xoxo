function createDefaults() {
    let config = {}
    if (!process.env.PGUSER) {
        config.user = 'swa';
        console.log('Please specify PGUSER env variable! [using default \'swa\']');
    }
    if (!process.env.PGHOST) {
        config.host = 'localhost';
        console.log('Please specify PGHOST env variable! [using default \'localhost\']')
    }
    if (!process.env.PGPASSWORD) {
        config.password = 'swa';
        console.log('Please specify PGPASSWORD env variable! [using default \'swa\']')
    }
    if (!process.env.PGDATABASE) {
        config.database = 'swa';
        console.log('Please specify PGDATABASE env variable! [using default \'swa\']')
    }
    if (!process.env.PGPORT) {
        config.port = 5432;
        console.log('Please specify PGPORT env variable! [using default \'5432\']')
    }
    return config;
}

const {Pool} = require('pg')

const FIND_BY_ID = 'select * from replays where id=$1'
const INSERT = 'insert into replays(player1id, player2id, winnerid, startingid, rounds, "date", completed, plays) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)'
const UPDATE = 'update replays set player1id=$1, player2id=$2, winnerid=$3, startingid=$4, rounds=$5, date=$6, completed=$7, plays=$8 where id=$9'
const DELETE = 'delete from replays where id=$1'

class PostgresService {
    constructor() {
        this.pool = new Pool(createDefaults())
        this.pool.on('error', (err, client) => {
            console.error('Unexpected error on idle client', err)
            process.exit(-1)
        })
    }

    findReplayById(id) {
        return this.pool.query(FIND_BY_ID, [id])
    }

    insertReplay({player1Id, player2Id, winnerId, startingId, rounds, date, completed, plays}) {
        return this.pool.query(INSERT, [player1Id, player2Id, winnerId, startingId, rounds, date, completed, plays])
    }

    putReplay(id, {player1Id, player2Id, winnerId, startingId, rounds, date, completed, plays}) {
        return this.pool.query(UPDATE, [player1Id, player2Id, winnerId, startingId, rounds, date, completed, plays, id])
    }

    deleteReplay(id) {
        return this.pool.query(DELETE, [id])
    }

    customQuery(sql, values) {
        return this.pool.query(sql, values)
    }
}

let inst = new PostgresService()

module.exports = inst
