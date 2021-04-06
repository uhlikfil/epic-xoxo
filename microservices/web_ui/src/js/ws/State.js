import store from "@/store";
import ModalOk from "@/components/modals/ModalOk";

export class State {
    constructor(context) {
        this.context = context
        this._expectsClose = false;
    }

    expectClose(bool) {
        this._expectsClose = bool
    }
    onOpen(e) {}
    onClose(e) {
        if (!this._expectsClose) {
            store.state.root.modal.forceReject()
            store.state.root.modal.show(ModalOk, {header: 'yikes', msg: 'cosik sa nam pokazilo'}, (x) => {store.state.root.$router.push('/')})
        }
    }
    onMessage(e) {}
    onError(e) {
        store.state.root.modal.forceReject()
        store.state.root.modal.show(ModalOk, {header: 'yikes', msg: 'cosik sa nam pokazilo'}, (x) => {store.state.root.$router.push('/')})
    }
}
