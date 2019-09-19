<template>
	<view>
		<!-- 话题介绍 -->
		<topic-info :item="topicInfo"></topic-info>
		<!-- tabbar切换 -->
		<swiper-tab-head
		:tabBars="tabBars" 
		:tabIndex="tabIndex" 
		@tabtap="tabtap"
		scrollStyle="border-bottom: 0"
		scrollItemStyle="width: 50%">
		</swiper-tab-head>
		<!-- 列表 -->
		<view class="topic-detail-list">
			<block v-for="(listitem, listindex) in tablist[tabIndex].list" :key="listindex">
				<common-list :item="listitem" :index="listindex"></common-list>
			</block>
		</view>
	</view>
</template>

<script>
	import topicInfo from "../../components/topic/topic-info.vue"
	import swiperTabHead from "../../components/index/swiper-tab-head.vue"
	import commonList from "../../components/common/common-list.vue"
	
	export default {
		components: {
			topicInfo,
			swiperTabHead,
			commonList
		},
		data() {
			return {
				topicInfo: {
					titlepic: "../../static/demo/topicpic/13.jpeg",
					title: "忆往事，敬余生",
					desc: "面试官：在电梯里巧遇马云你会怎么做？90后女孩的回答当初被录用",
					totalnum: 100,
					todaynum: 50
				},
				tabIndex: 0,
				tabBars: [
					{ name: "默认", id: "moren" },
					{ name: "最新", id: "zuixin" },
				],
				tablist: [
					{
						loadText: "上拉加载更多",
						list: [
							// 文字
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "哈哈",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是文字",
								titlepic: "",
								video: false,
								share: false,
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							},
							// 图文
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "哈哈",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是图文",
								titlepic: "../../static/demo/datapic/13.jpg",
								video: false,
								share: false,
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							},
							// 视频
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "哈哈",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是视频",
								titlepic: "../../static/demo/datapic/13.jpg",
								video: {
									looknum: 20,  // 单位w(万)
									long: "2:47"
								},
								share: false,
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							},
							// 分享
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "哈哈",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是分享",
								titlepic: "",
								video: false,
								share: {
									title: "分享标题",
									titlepic: "../../static/demo/datapic/14.jpg"
								},
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							}
						]
					},
					{
						loadText: "上拉加载更多",
						list: [
							// 文字
							{
								userpic: "../../static/demo/userpic/9.jpg",
								username: "嘿嘿",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是文字",
								titlepic: "",
								video: false,
								share: false,
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							},
							// 图文
							{
								userpic: "../../static/demo/userpic/9.jpg",
								username: "嘿嘿",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是图文",
								titlepic: "../../static/demo/datapic/14.jpg",
								video: false,
								share: false,
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							},
							// 视频
							{
								userpic: "../../static/demo/userpic/9.jpg",
								username: "嘿嘿",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是视频",
								titlepic: "../../static/demo/datapic/14.jpg",
								video: {
									looknum: 20,  // 单位w(万)
									long: "2:47"
								},
								share: false,
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							},
							// 分享
							{
								userpic: "../../static/demo/userpic/9.jpg",
								username: "嘿嘿",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是分享",
								titlepic: "",
								video: false,
								share: {
									title: "分享标题",
									titlepic: "../../static/demo/datapic/11.jpg"
								},
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							}
						]
					},
				]
			}
		},
		methods: {
			// tabbar点击事件
			tabtap(index) {
				this.tabIndex = index;
			}
		}
	}
</script>

<style>
</style>
