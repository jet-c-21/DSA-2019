package LinkedList;

class MyLinkedList {
	class Node {
		int data;
		Node nextNode;
		Node prevNode;

		public Node(int initVal) {
			this.data = initVal;
			nextNode = null;
			prevNode = null;
		}
	}

	int size;
	Node headNode;
	Node tailNode;

	public void addAtHead(int newHeadVal) {
		Node newNode = new Node(newHeadVal);
		if (headNode == null) {
			headNode = newNode;
			tailNode = newNode;
		} else {
			newNode.nextNode = headNode;
			headNode.prevNode = newNode;
			headNode = newNode;
		}
		size++;
	}

	public void addAtTail(int newTailVal) {
		Node newNode = new Node(newTailVal);
		if (headNode == null) {
			headNode = newNode;
			tailNode = newNode;
		} else {
			newNode.prevNode = tailNode;
			tailNode.nextNode = newNode;
			tailNode = newNode;
		}
		size++;
	}

	public void addAtIndex(int index, int newVal) {
		if (index <= 0) {
			addAtHead(newVal);
		} else if (index == size) {
			addAtTail(newVal);
		} else if (index < size) {
			Node newNode = new Node(newVal);		
			Node target = getNode(index);		
			newNode.nextNode = target;	
			newNode.prevNode = target.prevNode; //FIRST
			target.prevNode = newNode;
			
			// newNode.prevNode.nextNode�٬O����targetNode�n�令����newNode
			newNode.prevNode.nextNode = newNode; //SECOND
			size++;
		}
	}

	public void deleteAtIndex(int index) {
		if (index >= size || index < 0) {
			return;
		} else if (index == 0) {
			headNode = headNode.nextNode;
			if (headNode != null) {
				headNode.prevNode = null;
			}
		} else if (index == size - 1) {
			tailNode = tailNode.prevNode;
			if (tailNode != null) {
				tailNode.nextNode = null;
			}
		} else if (index < size - 1) {
			Node target = getNode(index);
			target.prevNode.nextNode = target.nextNode;
			target.nextNode.prevNode = target.prevNode;
		}
		size--;
	}

	public Node getNode(int index) {
		if (index >= size || index < 0) {
			return null;
		}
		// ����ڪ�index�t
		int tailDistance = size - 1 - index;
		int count = 0;
		Node temp;
		// �M�w�n�qhead�}�l��A�٬O�qtail
		if (index <= tailDistance) {
			temp = headNode;
			// ��ؼЦ�m���e�@�ӡA��next
			while (count < index) {
				temp = temp.nextNode;
				count++;
			}
		} else {
			temp = tailNode;
			while (count < tailDistance) {
				temp = temp.prevNode;
				count++;
			}
		}
		return temp;
	}

	public int get(int index) {
		Node target = getNode(index);
		return target != null ? target.data : -1;
	}
}