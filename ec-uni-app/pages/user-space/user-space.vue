<template>
	<view>
		<!-- 背景图+用户基本信息 -->
		<user-space-head :userinfo="userinfo"></user-space-head>
		<!-- 统计 -->
		<view class="user-space-data">
			<home-data :homedata="spacedata"></home-data>
		</view>
		<!-- 分隔线 -->
		<view style="height: 20rpx; background: #F4F4F4;"></view>
		<!-- tab导航 -->
		<swiper-tab-head
		:tabBars="tabBars" 
		:tabIndex="tabIndex"
		@tabtap="tabtap"
		scrollItemStyle="width:33.33%;"
		scrollStyle="border-bottom:0;">
		</swiper-tab-head>
		<!-- 主页 -->
		<block v-for="(item,index) in tablist" :key="index">
			<template v-if="tabIndex==0">
				<user-space-userinfo :userinfo="userinfo"></user-space-userinfo>
			</template>
			<template v-else-if="tabIndex==index">
				<!-- 列表 -->
				<block v-for="(list,listindex) in item.list" :key="listindex">
					<common-list :item="list" :index="listindex"></common-list>
				</block>
				<!-- 上拉加载 -->
				<load-more :loadText="item.loadText"></load-more>
			</template>
		</block>
		<!-- 操作菜单 -->
		<user-space-popup 
		:show="show" 
		@hide="toggleShow" 
		@lahei="lahei" 
		@beizhu="beizhu">
		</user-space-popup>
	</view>
</template>

<script>
	import userSpaceHead from "../../components/user-space/user-space-head.vue";
	import homeData from "../../components/home/home-data.vue";
	import swiperTabHead from "../../components/index/swiper-tab-head.vue";
	import userSpaceUserinfo from "../../components/user-space/user-space-userinfo.vue"
	import commonList from "../../components/common/common-list.vue";
	import loadMore from "../../components/common/load-more.vue";
	import userSpacePopup from "../../components/user-space/user-space-popup.vue"
	
	export default {
		components: {
			userSpaceHead,
			homeData,
			swiperTabHead,
			userSpaceUserinfo,
			commonList,
			loadMore,
			userSpacePopup
		},
		data() {
			return {
				show: false,
				userinfo: {
					bgimg: 1,
					userpic: "../../static/demo/userpic/11.jpg",
					username: "JIA一勺",
					sex: 0,
					age: 20,
					isguanzhu: false,
					regtime: "2019-04-11",
					id: 1213,
					birthday: "1987-02-07",
					job: "IT",
					path: "广东广州",
					qg: "已婚"
				},
				spacedata: [
					{ name: "获赞", num: "10k" },
					{ name: "关注", num: 11 },
					{ name: "粉丝", num: 12 }
				],
				tabIndex:0,
				tabBars:[
					{ name:"主页",id:"zhuye" },
					{ name:"糗事",id:"qiushi" },
					{ name:"动态",id:"dongtai" },
				],
				tablist: [
					{},
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
		// 上拉触底事件
		onReachBottom() {
			// 上拉加载
			this.loadMore();
		},
		onNavigationBarButtonTap(e) {
			if (e.index==0) {
				this.toggleShow();
			}
		},
		methods: {
			// 操作菜单显示隐藏
			toggleShow() {
				this.show = !this.show
			},
			// 拉黑
			lahei() {
				console.log("拉黑");
				this.toggleShow();
			},
			// 备注
			beizhu() {
				console.log("备注");
				this.toggleShow();
			},
			loadMore() {
				if (this.tablist[this.tabIndex].loadText != "上拉加载更多") {
					return;
				}
				// 修改状态
				this.tablist[this.tabIndex].loadText = "加载中...";
				// 获取数据
				setTimeout( () => {
					// 获取完成
					let obj = {
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
					};
					this.tablist[this.tabIndex].list.push(obj);
					this.tablist[this.tabIndex].loadText = "上拉加载更多";
				}, 1000)
				// this.tablist[this.tabIndex].loadText = "没有更多数据了";
			},
			tabtap(index){
				// console.log(index);
				this.tabIndex=index;
				// this.tablist[this.tabIndex].page = 1;
				// this.getList();
			}
		}
	}
</script>

<style>
	.user-space-margin {
		margin: 15rpx 0;
	}
	.user-space-data {
		position: relative;
		border-top-left-radius: 20rpx;
		border-top-right-radius: 20rpx;
		margin-top: -15rpx;
		background: #FFFFFF;
		z-index: 10;
	}
</style>
