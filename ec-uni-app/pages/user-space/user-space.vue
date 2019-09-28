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
		<user-space-userinfo :userinfo="userinfo"></user-space-userinfo>
	</view>
</template>

<script>
	import userSpaceHead from "../../components/user-space/user-space-head.vue";
	import homeData from "../../components/home/home-data.vue";
	import swiperTabHead from "../../components/index/swiper-tab-head.vue";
	import userSpaceUserinfo from "../../components/user-space/user-space-userinfo.vue"
	
	export default {
		components: {
			userSpaceHead,
			homeData,
			swiperTabHead,
			userSpaceUserinfo
		},
		data() {
			return {
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
				]
			}
		},
		methods: {
			tabtap(index){
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
