export class IndexItem {
    constructor(
        public userPic: string,
        public userName: string,
        public isGuanzhu: boolean,
        public title: string,
        public type: string,
        public infoNum: InfoNum,
        public commentNum: number,
        public shareNum: number,
        public titlePic: string,
        public playNum?: number,
        public long?: string
    ) {}
}

export class InfoNum {
    constructor(
        public index: number,
        public dingNum: number,
        public caiNum: number
    ) {}
}
