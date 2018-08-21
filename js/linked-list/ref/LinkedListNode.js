// import Comparator from '../../utils/comparator/Comparator';
// import Comparator from '../../utils/comparator/Comparator';
class Comparator {
    /**
     * @param {function(a: *, b: *)} [compareFunction]
     */
    constructor(compareFunction) {
        this.compare = compareFunction || Comparator.defaultCompareFunction;
    }

    /**
     * @param {(string|number)} a
     * @param {(string|number)} b
     * @returns {number}
     */
    static defaultCompareFunction(a, b) {
        if (a === b) {
            return 0;
        }

        return a < b ? -1 : 1;
    }

    equal(a, b) {
        return this.compare(a, b) === 0;
    }

    lessThan(a, b) {
        return this.compare(a, b) < 0;
    }

    greaterThan(a, b) {
        return this.compare(a, b) > 0;
    }

    lessThanOrEqual(a, b) {
        return this.lessThan(a, b) || this.equal(a, b);
    }

    greaterThanOrEqual(a, b) {
        return this.greaterThan(a, b) || this.equal(a, b);
    }

    reverse() {
        const compareOriginal = this.compare;
        this.compare = (a, b) => compareOriginal(b, a);
    }
}

// Node
// export default
class LinkedListNode {
    constructor(value, next) {
        this.value = value;
        this.next = next;
    }

    toString(callback) {
        // console.log(callback)
        return callback ? callback(this.value) : `${this.value}`;
    }
}

// Linked list constructor
class LinkedList {
    /**
     * @param {Function} [comparatorFunction]
     */
    constructor(comparatorFunction) {
        /** @var LinkedListNode */
        this.head = null;

        /** @var LinkedListNode */
        this.tail = null;

        this.compare = new Comparator(comparatorFunction);
    }

    /**
     * @param {*} value
     * @return {LinkedList}
     */
    prepend(value) {
        // Make new node to be a head.
        const newNode = new LinkedListNode(value, this.head);
        this.head = newNode;

        // If there is no tail yet let's make new node a tail.
        if (!this.tail) {
            this.tail = newNode;
        }

        return this;
    }


    /**
     * @param {Object} findParams
     * @param {*} findParams.value
     * @param {function} [findParams.callback]
     * @return {LinkedListNode}
     */
    find({value = undefined, callback = undefined}) {
        console.log(this.head); // All value in head
        if (!this.head) {
            return null;
        }

        let currentNode = this.head;

        while (currentNode) {
            // If callback is specified then try to find node by callback.
            if (callback && callback(currentNode.value)) {
                return currentNode;
            }

            // If value is specified then try to compare by value..
            if (value !== undefined && this.compare.equal(currentNode.value, value)) {
                return currentNode;
            }
            currentNode = currentNode.next;
        }

        return null;
    }

}

var l = new LinkedList()
l.prepend(32)
l.prepend(5)
console.log(l.find(6))