<template>
	<view>
		
		<view class="box">
			<view class="box-item">1</view>
			<view class="box-item">2</view>
			<view class="box-item">3</view>
			<view class="box-item">4</view>
			<view class="box-item">5</view>
			<view class="box-item">6</view>
		</view>
		
	</view>
	
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>
	
.box {
	width: 100%;
	height: 500upx;
	border: 1upx solid #CCCCCC;
	display: flex;
	flex-wrap: wrap;
	/* flex-wrap: wrap-reverse; */
	justify-content: center;
	align-items: center;
}

.box-item {
	color: #FFFFFF;
	height: 200upx;
	width: 200upx;
	line-height: 200upx;
	font-size: 30upx;
	font-weight: bold;
	text-align: center;
}

.box-item:nth-of-type(odd) {
	background: #007AFF;
}

.box-item:nth-of-type(even) {
	background: #09BB07;
}

</style>
