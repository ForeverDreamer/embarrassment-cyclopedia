<template>
	<view>
		<!-- 自定义导航栏 -->
		<uni-nav-bar fixed="true" status-bar="true" @click-right="openAdd" >
			<!-- 左边 -->
			<view slot="left" class="nav-left">
				<view class="icon iconfont icon-qiandao"></view>
			</view>
			<!-- 中间 -->
			<view class="nav-tab-bar u-f-ajc">
				<block v-for="(tab, index) in tabBars" :key="tab.id">
					<view class="u-f-ajc" :class="{'active': tabIndex==index}" @tap="changeTab(index)">
						{{tab.name}}
						<view v-if="tabIndex==index" class="nav-tab-bar-line"></view>
					</view>
				</block>
			</view>
			<!-- 右边 -->
			<view  slot="right" class="nav-right u-f-ajc">
				<view class="icon iconfont icon-bianji1"></view>
			</view>
		</uni-nav-bar>
		<!-- 列表 -->
		<block v-for="(item, index) in list" :key="index">
			<common-list :item="item" :index="index"></common-list>
		</block>
	</view>
</template>

<script>
	import uniNavBar from "../../components/uni-nav-bar/uni-nav-bar.vue"
	import commonList from "../../components/common/common-list.vue"
	
	export default {
		components: {
			uniNavBar,
			commonList
		},
		data() {
			return {
				tabIndex: 0,
				tabBars: [
					{name: "关注", id: "guanzhu"},
					{name: "话题", id: "topic"}
				],
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
			}
		},
		methods: {
			changeTab(index) {
				this.tabIndex = index;
			},
			openAdd() {
				// 打开发布页面
				uni.navigateTo({
					url: '../add-input/add-input'
				});
			}
		}
	}
</script>

<style>
/* 	.nav-left, .nav-right {
		border: 1rpx solid;
	} */
	.nav-left>view, .nav-right>view {
		font-size: 40rpx;
	}
	.nav-left>view {
		color: #FF9619;
	}
	.nav-left {
		margin-left: 16rpx;
	}
	.nav-right {
		width: 100%;
	}
	.nav-tab-bar {
		width: 100%;
		margin-left: -30rpx;
		position: relative;
	}
	.nav-tab-bar>view {
/* 		border: 1rpx solid; */
		font-size: 32rpx;
		padding: 0 15rpx;
		font-weight: bold;
		color: #969696;
	}
	.active {
		color: #333333!important;
	}
	.nav-tab-bar-line {
		border-bottom: 5rpx solid #FEDE33;
		border-top: 5rpx solid #FEDE33;
		width: 70rpx;
		border-radius: 20rpx;
		position: absolute;
		bottom: 5rpx;
	}
</style>
