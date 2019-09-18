<template>
	<view>
		<!-- 自定义导航栏 -->
		<news-nav-bar :tabBars="tabBars" :tabIndex="tabIndex" @change-tab="changeTab"></news-nav-bar>
		<view class="uni-tab-bar">
			<swiper class="swiper-box" 
			:style="{height:swiperHeight+'px'}" 
			:current="tabIndex" 
			@change="tabChange">
				<!-- 关注 -->
				<swiper-item>
					<scroll-view scroll-y class="list">
						<block v-for="(item, index) in list" :key="index">
							<common-list :item="item" :index="index"></common-list>
						</block>
					</scroll-view>
				</swiper-item>
				<!-- 话题 -->
				<swiper-item>
					<scroll-view scroll-y class="list">
					话题
					</scroll-view>
				</swiper-item>
			</swiper>
		</view>
	</view>
</template>

<script>
	import newsNavBar from "../../components/news/news-nav-bar.vue"
	import commonList from "../../components/common/common-list.vue"
	
	export default {
		components: {
			newsNavBar,
			commonList
		},
		data() {
			return {
				swiperHeight: 500,
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
		onLoad() {
			uni.getSystemInfo({
				success: (res) => {
					this.swiperHeight = res.windowHeight - uni.upx2px(100)
				}
			})
		},
		methods: {
			// 点击切换
			changeTab(index) {
				this.tabIndex = index;
			},
			// 滑动事件
			tabChange(e) {
				this.tabIndex = e.detail.current;
			}
		}
	}
</script>

<style>

</style>
