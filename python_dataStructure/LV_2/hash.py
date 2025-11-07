#4. Hash Table문제
    #1) hash -> 체이닝------------------------------------------------------------------------------------------------
class HashTableChaining:
    def __init__(self,size=5):
        self.size = size
        # _는 사용 안하는 변수
        # 저 형태는 리스트 안에 []를 사이즈크기 만큼 개수로 넣겠다
        self.table = [[] for _ in range(size)]

    def _hash(self,key):
        return hash(key)%self.size
    
    def insert(self,key,value):
        index = self._hash(key)
        bucket = self.table[index]
        # 같은 key가 들어오면 value만 업데이트
        for i, (k,v) in  enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
        # 이게 본 함수 
        bucket.append((key,value))

    def delete(self,key):
        index = self._hash(key)
        bucket = self.table[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                    #del은 참조를 없애는 것으로
                        #bucket[i]였던 존재를 없앰 (변수에 할당된 값 없애기도 가능)
                return True
        return False
    
    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def show(self):
        print("---체이닝 해시 결과---")
        for i, bucket in enumerate(self.table):
            print(f"[{i}] : {bucket}")

h = HashTableChaining(3)
h.insert("apple", 100)
h.insert("banana", 200)
h.insert("grape", 300)
h.insert("peach", 400)
h.insert("melon", 500)  # 충돌 발생 가능
h.show()
h.delete("apple")
print(f"grape의 검색 결과", h.search("grape"))
h.show()

    #2) hash -> 선형탐사(개방 주소법)------------------------------------------------------------------------------------------------
class HashTableLinear:
    def __init__(self, size=5):
        self.size = size
        # None으로 한칸에 한 데이터만 있도록 처리
        self.table = [None] * size  

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        # 모든 칸을 뒤졌을 때 다시 처음으로 온 걸 인지하시 위함(무한방지)
        original_index = index
        
        # 만약 이미 무가 이미 들어있으면
        while self.table[index] is not None:
            stored_key, _ = self.table[index]
            if stored_key == key:
                # 이미 존재하는 키라면 값 업데이트
                self.table[index] = (key, value)
                return
            # 그냥 겹친거면 다른 칸 이동 해보기
            index = (index + 1) % self.size
            if index == original_index:
                print("테이블이 가득 찼습니다.")
                return
        #본 함수
        self.table[index] = (key, value)

    def search(self, key):
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            stored_key, value = self.table[index]
            if stored_key == key:
                return value
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def show(self):
        print("---선형탐사  해시 결과---")
        for i, item in enumerate(self.table):
            print(f"{i}: {item}")

h = HashTableLinear(5)
h.insert("apple", 100)
h.insert("banana", 200)
h.insert("grape", 300)
h.insert("melon", 400)
h.insert("peach", 500)
h.show()

    #3) hash -> 이중해싱(개방 주소법)------------------------------------------------------------------------------------------------
#선형 탐사는 인덱스를 한칸씩 옮기는거라면
#이중 해싱은 보조 해시값을 하나 더 사용하여 인덱스 값을 결정한다
class HashTableDouble:
    def __init__(self, size=7):
        self.size = size
        self.table = [None] * size

    def _hash1(self, key):
        return hash(key) % self.size

    def _hash2(self, key):
        # 보조 해시: 0이 되지 않게 1~(size-1) 범위
        #나누는 값을 달리해서 해시값을 바꿈.
        return 1 + (hash(key) % (self.size - 1))

    def insert(self, key, value):
        index = self._hash1(key)
        step = self._hash2(key)
        i = 0

        while self.table[index] is not None:
            stored_key, _ = self.table[index]
            if stored_key == key:
                # 키가 같으면 업데이트
                self.table[index] = (key, value)
                return
            i += 1
            index = (index + step) % self.size
            if i >= self.size:
                print("테이블이 가득 찼습니다.")
                return
        self.table[index] = (key, value)

    def search(self, key):
        index = self._hash1(key)
        step = self._hash2(key)
        i = 0

        while self.table[index] is not None and i < self.size:
            stored_key, value = self.table[index]
            if stored_key == key:
                return value
            i += 1
            index = (index + step) % self.size
        return None

    def show(self):
        print("---이중해시 결과---")
        for i, item in enumerate(self.table):
            print(f"{i}: {item}")

h = HashTableDouble(7)
h.insert("apple", 100)
h.insert("banana", 200)
h.insert("grape", 300)
h.insert("peach", 400)
h.insert("melon", 500)
h.insert("cherry", 600)

h.show()

print("apple:", h.search("apple"))
print("cherry:", h.search("cherry"))
print("pineapple:", h.search("pineapple"))
