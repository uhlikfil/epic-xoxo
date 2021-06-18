const service = require('./../service/ReplayService')
const ass = require('assert')
const axios = require('axios')

describe('Adding a replay', () => {
    it('should add valid replay', function (done) {
        service.add_replay({
            player1Id: '1',
            player2Id: '2',
            winnerId: '2',
            startingId: '2',
            rounds: 40,
            date: new Date().toISOString(),
            completed: true,
            plays: []
        })
            .then((data) => {
                done()
            })
            .catch((err) => {
                ass.fail(err)
            })
    });
    it('should NOT add valid replay', function (done) {
        service.add_replay({
            player1Id: '1',
            player2Id: '2',
            winnerId: '2',
            startingId: '2',
            rounds: 40,
            plays: []
        })
            .then((data) => {
                ass.fail()
            })
            .catch((err) => {
                done()
            })
    });
})
describe('Getting a replay', () => {
    it('get a replay', function (done) {
        service.get_replay_by_id(1)
            .then((data) => {
                done()
            })
            .catch((err) => {
                done(new Error(err))
            })
    });
})
describe('Filtering works', ()=>{
    it('should fitler the replays', (done)=>{
        service.filter_replays({completed:true})
            .then((data)=>{
                if (data.length > 0) {done()}
            })
            .catch((err)=>{
                done(new Error(err))
            })
    })
    it('should fitler out all the replays', (done)=>{
        service.filter_replays({completed: false})
            .then((data)=>{
                console.log(data);
                if (data.length == 0) {done()}
                else done (new Error('Did not filter.'))
            })
            .catch((err)=>{
                done(new Error(err))
            })
    })
})
